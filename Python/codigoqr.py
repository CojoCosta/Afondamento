
#-------------------------------CODIGO QR----------------------------------#
import pyqrcode
# Cadena de la que queremos generar el QR
s = "https://github.com/CojoCosta"
# Generación
url = pyqrcode.create(s)
# Se guarda como png
url.png("myqr.png", scale=6)