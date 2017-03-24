from PIL import Image

ov_image = Image.open("337.jpg")
square_ov_image = ov_image.resize((100,100))
flip_ov_image = ov_image.transpose(Image.FLIP_TOP_BOTTOM)
spin_ov_image = ov_image.transpose(Image.ROTATE_90)

ov_image.show()
square_ov_image.show()
flip_ov_image.show()
spin_ov_image.show()