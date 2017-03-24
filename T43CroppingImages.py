from PIL import Image

img = Image.open("337.jpg")
area = (100,100,200,200)
cropped_img = img.crop(area)

#img.show()
cropped_img.show()