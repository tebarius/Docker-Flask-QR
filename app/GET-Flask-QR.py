#!/usr/bin/env python3
# notwendige pakete via pip:
# pip install Flask-QRcode waitress
from flask import Flask, render_template, request
from flask_qrcode import QRcode

app = Flask(__name__, static_folder='qr-static', template_folder='get-templates')
QRcode(app)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/index.html")
def index_html():
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


@app.route("/mecard.html")
def mecard():
    return render_template('mecard.html')


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

    elif request.args.get('type') == "geo":
        data = "GEO:"
        if request.args.get('ns') == "S":
            data += "-"
        data += f"{request.args.get('nsk')},"
        if request.args.get('we') == "W":
            data += "-"
        data += f"{request.args.get('wek')}"
        if request.args.get('high') != "":
            data += f",{request.args.get('high')}"
    elif request.args.get('type') == "mecard":
        titel = request.args.get("titel")
        if titel != "":
            titel += " "
        data = (f"MECARD:N:{request.args.get('nname')},{titel}{request.args.get('vname')};"
                f"ADR:{request.args.get('pbox')},{request.args.get('adresszusatz')},"
                f"{request.args.get('strasse')},{request.args.get('ort')},{request.args.get('bland')},"
                f"{request.args.get('plz')},{request.args.get('land')};")
        if request.args.get('tel') != "":
            data += f"TEL:{request.args.get('tel')};"
        if request.args.get('mail') != "":
            data += f"EMAIL:{request.args.get('mail')};"
        if request.args.get('url') != "":
            data += f"URL:{request.args.get('url')};"
        if request.args.get('tel') != "":
            data += f"TEL:{request.args.get('tel')};"
        if request.args.get('nickname') != "":
            data += f"NICKNAME:{request.args.get('nickname')};"
        if request.args.get('gebdate') != "":
            data += f"BDAY:{request.args.get('gebdate').replace('-', '')};"
        if request.args.get('note') != "":
            data += f"NOTE:{request.args.get('note')};"
    elif request.args.get('type') == "vcard":
        # BEGIN:VCARD
        # VERSION:3.0
        # N:Nachname;Vorname;;Titel;
        # FN:Titel Vorname Nachname
        # ORG:Firma
        # TITLE:Job-Titel(Funktion)
        # ADR:Postfach;Adresszusatz;straße;stadt;Bundesland;plz;Land
        # TEL;TYPE=VOICE,WORK:Telefon
        # TEL;TYPE=CELL,WORK:Mobil
        # TEL;TYPE=VOICE,HOME:Telefon
        # TEL;TYPE=CELL,HOME:Mobil
        # TEL;TYPE=FAX:Fax
        # EMAIL;TYPE=WORK:E-Mail
        # EMAIL;TYPE=HOME:E-Mail
        # URL:website
        # BDAY:--0203
        # NICKNAME:spitzname
        # END:VCARD
        titel = request.args.get("titel")
        if titel != "":
            titel += " "
        data = (f"BEGIN:VCARD\nVERSION:3.0\nN:{request.args.get('nname')};"
                f"{request.args.get('vname')};;{titel};\nFN:{titel}"
                f"{request.args.get('vname')} {request.args.get('nname')}\n"
                f"ADR:{request.args.get('pbox')};{request.args.get('adresszusatz')};"
                f"{request.args.get('strasse')};{request.args.get('ort')};"
                f"{request.args.get('bland')};{request.args.get('plz')};"
                f"{request.args.get('land')}\n")
        if request.args.get("org") != "":
            data += f"ORG:{request.args.get('org')}\n"
        if request.args.get("jtitel") != "":
            data += f"TITLE:{request.args.get('jtitel')}\n"
        if request.args.get("tel-a") != "":
            data += f"TEL;TYPE=VOICE,WORK:{request.args.get('tel-a')}\n"
        if request.args.get("mobil-a") != "":
            data += f"TEL;TYPE=CELL,WORK:{request.args.get('mobil-a')}\n"
        if request.args.get("tel-p") != "":
            data += f"TEL;TYPE=VOICE,HOME:{request.args.get('tel-p')}\n"
        if request.args.get("mobil-p") != "":
            data += f"TEL;TYPE=CELL,HOME:{request.args.get('mobil-p')}\n"
        if request.args.get("fax") != "":
            data += f"TEL;TYPE=FAX:{request.args.get('fax')}\n"
        if request.args.get("mail-a") != "":
            data += f"EMAIL;TYPE=WORK:{request.args.get('mail-a')}\n"
        if request.args.get("mail-p") != "":
            data += f"EMAIL;TYPE=HOME:{request.args.get('mail-p')}\n"
        if request.args.get("url") != "":
            data += f"URL:{request.args.get('url')}\n"
        if request.args.get("nickname") != "":
            data += f"NICKNAME:{request.args.get('nickname')}\n"
        if request.args.get("gebdate") != "":
            gebdate = request.args.get('gebdate').replace('-', '')
            if request.args.get("ohneJahr"):
                data += f"BDAY:--{gebdate[4:]}\n"
            else:
                data += f"BDAY:{gebdate}\n"
        data += "END:VCARD\n"
    elif request.args.get('type') == "wifi":
        passw = (request.args.get("passw").replace("\\", "\\\\").replace(";", "\\;")
                 .replace(",", "\\,").replace(":", "\\:").replace("\"", "\\\""))
        ssid = (request.args.get("ssid").replace("\\", "\\\\").replace(";", "\\;")
                .replace(",", "\\,").replace(":", "\\:").replace("\"", "\\\""))
        if request.args.get("auth") == "WPA":
            data = f'WIFI:T:WPA;S:"{ssid}";P:"{passw}";'
        else:
            data = f'WIFI:T:nopass;S:"{ssid}";'
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
    # app.run(host='0.0.0.0', port=8002)
    from waitress import serve
    print("http://localhost:8002")
    serve(app, host="0.0.0.0", port=8002)
