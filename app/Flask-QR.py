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


@app.route("/qr.html")
def makeqr():
    data = request.args.get('qr')
    return render_template('qr.html', data=data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
