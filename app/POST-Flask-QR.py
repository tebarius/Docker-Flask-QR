#!/usr/bin/env python3
# notwendige pakete via pip:
# pip install Flask-QRcode waitress
from flask import Flask, render_template, request
from flask_qrcode import QRcode

app = Flask(__name__, static_folder='qr-static', template_folder='post-templates')
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


@app.route("/qr.html", methods=['POST'])
def makeqr():
    data = "Sorry kein Inhalt!!!"
    if request.form['type'] == "text":
        data = request.form['text']

    elif request.form['type'] == "url":
        data = request.form['url']

    elif request.form['type'] == "tel":
        data = f"tel:{request.form['tel']}"

    elif request.form['type'] == "geo":
        data = "GEO:"
        if request.form['ns'] == "S":
            data += "-"
        data += f"{request.form['nsk']},"
        if request.form['we'] == "W":
            data += "-"
        data += f"{request.form['wek']}"
        if request.form['high'] != "":
            data += f",{request.form['high']}"
    elif request.form['type'] == "mecard":
        titel = request.form["titel"]
        if titel != "":
            titel += " "
        data = (f"MECARD:N:{request.form['nname']},{titel}{request.form['vname']};"
                f"ADR:{request.form['pbox']},{request.form['adresszusatz']},"
                f"{request.form['strasse']},{request.form['ort']},{request.form['bland']},"
                f"{request.form['plz']},{request.form['land']};")
        if request.form['tel'] != "":
            data += f"TEL:{request.form['tel']};"
        if request.form['mail'] != "":
            data += f"EMAIL:{request.form['mail']};"
        if request.form['url'] != "":
            data += f"URL:{request.form['url']};"
        if request.form['tel'] != "":
            data += f"TEL:{request.form['tel']};"
        if request.form['nickname'] != "":
            data += f"NICKNAME:{request.form['nickname']};"
        if request.form['gebdate'] != "":
            data += f"BDAY:{request.form['gebdate'].replace('-', '')};"
        if request.form['note'] != "":
            data += f"NOTE:{request.form['note']};"
    elif request.form['type'] == "vcard":
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
        titel = request.form["titel"]
        if titel != "":
            titel += " "
        data = (f"BEGIN:VCARD\nVERSION:3.0\nN:{request.form['nname']};"
                f"{request.form['vname']};;{titel};\nFN:{titel}"
                f"{request.form['vname']} {request.form['nname']}\n"
                f"ADR:{request.form['pbox']};{request.form['adresszusatz']};"
                f"{request.form['strasse']};{request.form['ort']};"
                f"{request.form['bland']};{request.form['plz']};"
                f"{request.form['land']}\n")
        if request.form["org"] != "":
            data += f"ORG:{request.form['org']}\n"
        if request.form["jtitel"] != "":
            data += f"TITLE:{request.form['jtitel']}\n"
        if request.form["tel-a"] != "":
            data += f"TEL;TYPE=VOICE,WORK:{request.form['tel-a']}\n"
        if request.form["mobil-a"] != "":
            data += f"TEL;TYPE=CELL,WORK:{request.form['mobil-a']}\n"
        if request.form["tel-p"] != "":
            data += f"TEL;TYPE=VOICE,HOME:{request.form['tel-p']}\n"
        if request.form["mobil-p"] != "":
            data += f"TEL;TYPE=CELL,HOME:{request.form['mobil-p']}\n"
        if request.form["fax"] != "":
            data += f"TEL;TYPE=FAX:{request.form['fax']}\n"
        if request.form["mail-a"] != "":
            data += f"EMAIL;TYPE=WORK:{request.form['mail-a']}\n"
        if request.form["mail-p"] != "":
            data += f"EMAIL;TYPE=HOME:{request.form['mail-p']}\n"
        if request.form["url"] != "":
            data += f"URL:{request.form['url']}\n"
        if request.form["nickname"] != "":
            data += f"NICKNAME:{request.form['nickname']}\n"
        if request.form["gebdate"] != "":
            gebdate = request.form['gebdate'].replace('-', '')
            if request.form["ohneJahr"]:
                data += f"BDAY:--{gebdate[4:]}\n"
            else:
                data += f"BDAY:{gebdate}\n"
        data += "END:VCARD\n"
    elif request.form['type'] == "wifi":
        passw = (request.form["passw"].replace("\\", "\\\\").replace(";", "\\;")
                 .replace(",", "\\,").replace(":", "\\:").replace("\"", "\\\""))
        ssid = (request.form["ssid"].replace("\\", "\\\\").replace(";", "\\;")
                .replace(",", "\\,").replace(":", "\\:").replace("\"", "\\\""))
        if request.form["auth"] == "WPA":
            data = f'WIFI:T:WPA;S:"{ssid}";P:"{passw}";'
        else:
            data = f'WIFI:T:nopass;S:"{ssid}";'
        if 'ssid_hidden' in request.form:
            data += "H:true;;"
        else:
            data += ";"

    elif request.form['type'] == "cal":
        # Format für Calendar (Zeilenumbrüche beachten!!):
        # BEGIN:VEVENT
        # SUMMARY:<titel>
        # DESCRIPTION:<beschreibung>
        # LOCATION:<Ort>
        # DTSTART:20231114T090000
        # DTEND:20231123T110000
        # END:VEVENT
        sdt = request.form['sdate'].replace('-', '')
        if request.form['edate'] == "":
            edt = sdt
        else:
            edt = request.form['edate'].replace('-', '')
        if request.form['stime'] != "":
            sdt += f"T{request.form['stime'].replace(':', '')}00"
        if request.form['etime'] != "":
            edt += f"T{request.form['etime'].replace(':', '')}00"
        data = (f"BEGIN:VEVENT\nSUMMARY:{request.form['title']}\n"
                f"DESCRIPTION: {request.form['description']}\n"
                f"LOCATION:{request.form['location']}\n"
                f"DTSTART:{sdt}\nDTEND:{edt}\n"
                f"END:VEVENT")
    elif request.form['type'] == "mail":
        more = False
        data = f"mailto:{request.form['mail']}"
        if request.form['cc'] != "":
            data += f"?cc={request.form['cc']}"
            more = True
        if request.form['bcc'] != "":
            if more:
                data += "&"
            else:
                data += "?"
                more = True
            data += f"bcc={request.form['bcc']}"
        if request.form['subject'] != "":
            if more:
                data += "&"
            else:
                data += "?"
                more = True
            data += f"subject={request.form['subject']}"
        if request.form['body'] != "":
            if more:
                data += "&"
            else:
                data += "?"
            data += f"body={request.form['body']}"
    return render_template('qr.html', data=data)


if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=8002)
    from waitress import serve
    print("http://localhost:8002")
    serve(app, host="0.0.0.0", port=8002)
