import qrcode
data = "https://www.twitch.tv/risadaaranha"
img = qrcode.make(data)
img.save("qrcode.png")