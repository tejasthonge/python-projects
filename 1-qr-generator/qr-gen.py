
#import qrcode
import qrcode as qr

#img = qrcode.make()

img =qr.make("https://www.linkedin.com/in/tejasthonge/")
img.save("tejas_linkdin.png")

