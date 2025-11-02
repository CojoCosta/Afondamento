
#-------------------------------CODIGO QR----------------------------------#
import pyqrcode
# Cadena de la que queremos generar el QR
s = "https://www.instagram.com/andrea_tesouro/"
# Generación
url = pyqrcode.create(s)
# Se guarda como png
url.png("myqr.png", scale=6)