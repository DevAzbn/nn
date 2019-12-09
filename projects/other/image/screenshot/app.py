from PIL import Image, ImageGrab
img = ImageGrab.grab()
img.save("screen.bmp", "BMP")
print(img.mode)

img2 = ImageGrab.grab( (100, 100, 300, 300) )
img2.save("screen2.bmp", "BMP")
print(img2.size)
