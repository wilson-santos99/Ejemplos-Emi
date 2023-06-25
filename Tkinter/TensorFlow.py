import qrcode
# URL de la página web

url = "pega tu url acá"
# Generar el código QR

img = qrcode.make(url)
# Guardar el código QR en un archivo

img.save("codigo_qr.png")
