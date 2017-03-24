from PIL import Image

a_img = Image.open("a.png")
c_img = Image.open("c.png")

area = (0,0,32,32)
a_img.paste(c_img,area)

a_img.show()

