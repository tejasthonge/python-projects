
#import qrcode
import qrcode as qr

#img = qrcode.make()
url = input("enter the url :")

img =qr.make(url)
img.save("qrcode.png")

