# Flask QR-Code-Generator

Dieses Programm benötigt Python und das Flask-Framework um einen kleinen Server auf Port 80
aufzumachen.

    pip install Flask-QRcode
... installiert alles Notwendige nach damit das Programm läuft

## Docker
2 unterschiedliche Dockerfile's, da obwohl bei beiden python:slim als Basis genutzt wird,
noch die Installation von ein paar packages zusätzlich notwendig ist, damit flask auch auf
dem RaspberryPi 3 via pip install integriert werden kann