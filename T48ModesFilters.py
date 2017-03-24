from PIL import Image
from PIL import ImageFilter

ov_img = Image.open("337.jpg")
black_white = ov_img.convert("L")
blur = ov_img.filter(ImageFilter.BLUR)
detail = ov_img.filter(ImageFilter.DETAIL)
edges = ov_img.filter(ImageFilter.FIND_EDGES)

black_white.show()
blur.show()
detail.show()
edges.show()

