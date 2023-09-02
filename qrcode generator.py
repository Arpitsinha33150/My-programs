import pyqrcode
l=input("Enter the link: ")
k= pyqrcode.create(l)
k.png('qrcode.png',scale = 10)
import os
os.system('qrcode.png')