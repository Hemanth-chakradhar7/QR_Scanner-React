import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

myqr = qrcode.make("linkedin.com/in/hemanth-chakradhar-chintala-2426492bb")
myqr1= qrcode.make("https://github.com/Hemanth-chakradhar7")
myqr.save("myqr.png",scale=8)
myqr1.save("myqr1.png",scale=8)
b = decode(Image.open("myqr.png"))
print(b[0].data.decode("ascii"))