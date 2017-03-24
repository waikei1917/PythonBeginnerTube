from PIL import Image

img = Image.open("337.jpg")
print(img.size)
print(img.format)

img.show()