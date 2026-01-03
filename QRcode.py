import qrcode
data = "Insira o link aqui"
img = qrcode.make(data)
img.save("qrcode.png")
