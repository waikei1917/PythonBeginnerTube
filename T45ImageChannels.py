from PIL import Image

a_img = Image.open("a.png")
print(a_img.mode)

r1,g1,b1,a1 = a_img.split()
'''
r.show()
g.show()
b.show()
a.show()
'''

#new_img = Image.merge("RGB",(b,g,r))
#new_img.show()

b_img = Image.open("b.png")
print(b_img.mode)

r2,g2,b2,a2 = b_img.split()

new_img = Image.merge("RGB",(r2,g1,b2))
new_img.show()
