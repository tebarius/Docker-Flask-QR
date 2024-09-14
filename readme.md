# Flask QR-Code-Generator
Sorry folks, because this project startet as experiment for Flask and Docker only german description and manual. 

HTTP-Server auf Port 8002 mit QR-Code-Generator zur Generierung verschiedener Arten von QR-Codes (Text, URL, Mail,
Tel., WIFI, Kalender-Event, vCard, MeCard).

Eigentlich ist das Projekt für mich ein Experimentierfeld gewesen um mal Flask ein bisschen auszuprobieren 

## ohne Docker
Um lokal das ganze zu testen werden nur die Dateien aus dem app-Verzeichnis benötigt. 
Voraussetzung ist eine funktionierende Python Installation und das Flask-Framework inclusive Flask-QRcode welches sich
recht einfach über die Konsole mit ...  

    pip install Flask-QRcode
... installieren lässt.  
  
Zum Starten dann eine der beiden .py Dateien benutzen, je nachdem welcher
HTTP-Modus gewollt ist. Im Zweifelsfall POST ... nehmen und wenn ein Doppelklick nicht geht dann halt über 
die Konsole: `python POST-Flask-QR.py`

Der Server ist dann via http://localhost:8002 zu erreichen

## Docker
Ab Version 1.3.0 des Containers ist es ein Multi-Architektur-DockerContainer für AMD64, ARM64, i386 und ARMv7

In der Standardeinstellung werden die Formulare mit HTTP-POST-Anfragen gesendet/verarbeitet.  
Sollte es Gründe geben, warum gewünscht wird, dass dies der HTTP-GET-Variante zu machen, lässt sich das über die
Enviroment Variable `HTTP_METHOD` ändern.

## Enviroment-Variablen

- `HTTP_METHOD` GET oder POST (default: POST)

## Docker Installation/Start

### Installation
siehe https://hub.docker.com/r/tebarius/flask-qrcode-generator  

oder via Github-Docker-Registry:
- einfacher Start:  
  `docker run -d -p 8002:8002 ghcr.io/tebarius/flask-qrcode-generator:latest`  
  erreichbar dann z.B. via http://localhost:8002
- mit HTTP-Methode GET auf Port 80:  
  `docker run -d -p 80:8002 -e HTTP_METHOD=GET ghcr.io/tebarius/flask-qrcode-generator:latest`  
  erreichbar dann z.B. via http://localhost
