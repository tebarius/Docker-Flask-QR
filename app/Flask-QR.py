#!/usr/bin/env python3
# notwendige pakete via pip:
# pip install Flask Flask-QRcode
from flask import Flask, render_template, request
from flask_qrcode import QRcode

app = Flask(__name__)
QRcode(app)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/text.html")
def text():
    return render_template('text.html')


@app.route("/tel.html")
def tel():
    return render_template('tel.html')


@app.route("/url.html")
def url():
    return render_template('url.html')


@app.route("/vcard.html")
def vcard():
    return render_template('vcard.html')


@app.route("/geo.html")
def geo():
    return render_template('geo.html')


@app.route("/mail.html")
def mail():
    return render_template('mail.html')


@app.route("/wifi.html")
def wifi():
    return render_template('wifi.html')


@app.route("/cal.html")
def cal():
    return render_template('cal.html')


@app.route("/qr.html")
def makeqr():
    data = "Sorry kein Inhalt!!!"
    if request.args.get('type') == "text":
        data = request.args.get('text')

    elif request.args.get('type') == "url":
        data = request.args.get('url')

    elif request.args.get('type') == "tel":
        data = f"tel:{request.args.get('tel')}"

    elif request.args.get('type') == "vcard":
        #BEGIN:VCARD
        #VERSION:3.0
        #N:Nachname;Vorname;;Titel;
        #FN:Titel Vorname Nachname
        #ORG:Firma
        #TITLE:Job-Titel(Funktion)
        #ADR:Postfach;Adresszusatz;straße;stadt;Bundesland;plz;Land
        #TEL;TYPE=VOICE,WORK:Telefon
        #TEL;TYPE=CELL,WORK:Mobil
        #TEL;TYPE=VOICE,HOME:Telefon
        #TEL;TYPE=CELL,HOME:Mobil
        #TEL;FAX:Fax
        #EMAIL;TYPE=WORK:E-Mail
        #EMAIL;TYPE=HOME:E-Mail
        #URL:website
        #BDAY:--0203
        #NICKNAME:spitzname
        #END:VCARD
        pass

    elif request.args.get('type') == "geo":
        pass

    elif request.args.get('type') == "wifi":
        passw = (request.args.get("passw").replace("\\", "\\\\").replace(";", "\\;")
                 .replace(",", "\\,").replace(":", "\\:").replace("\"", "\\\""))
        ssid = (request.args.get("ssid").replace("\\", "\\\\").replace(";", "\\;")
                .replace(",", "\\,").replace(":", "\\:").replace("\"", "\\\""))
        if request.args.get("auth") == "WPA":
            data = f'WIFI:T:WPA;S:"{ssid}";P:"{passw}"'
        else:
            data = f'WIFI:T:nopass;S:"{ssid}"'
        if request.args.get("hidden"):
            data += "H:true;;"
        else:
            data += ";"
    elif request.args.get('type') == "cal":
        # Format für Calendar (Zeilenumbrüche beachten!!):
        # BEGIN:VEVENT
        # SUMMARY:<titel>
        # DESCRIPTION:<beschreibung>
        # LOCATION:<Ort>
        # DTSTART:20231114T090000
        # DTEND:20231123T110000
        # END:VEVENT
        sdt = request.args.get('sdate').replace('-', '')
        if request.args.get('edate') == "":
            edt = sdt
        else:
            edt = request.args.get('edate').replace('-', '')
        if request.args.get('stime') != "":
            sdt += f"T{request.args.get('stime').replace(':', '')}00"
        if request.args.get('etime') != "":
            edt += f"T{request.args.get('etime').replace(':', '')}00"
        data = (f"BEGIN:VEVENT\nSUMMARY:{request.args.get('title')}\n"
                f"DESCRIPTION: {request.args.get('description')}\n"
                f"LOCATION:{request.args.get('location')}\n"
                f"DTSTART:{sdt}\nDTEND:{edt}\n"
                f"END:VEVENT")

    elif request.args.get('type') == "mail":
        more = False
        data = f"mailto:{request.args.get('mail')}"
        if request.args.get('cc') != "":
            data += f"?cc={request.args.get('cc')}"
            more = True
        if request.args.get('bcc') != "":
            if more:
                data += "&"
            else:
                data += "?"
                more = True
            data += f"bcc={request.args.get('bcc')}"
        if request.args.get('subject') != "":
            if more:
                data += "&"
            else:
                data += "?"
                more = True
            data += f"subject={request.args.get('subject')}"
        if request.args.get('body') != "":
            if more:
                data += "&"
            else:
                data += "?"
            data += f"body={request.args.get('body')}"
    return render_template('qr.html', data=data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
