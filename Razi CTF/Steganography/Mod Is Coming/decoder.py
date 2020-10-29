from numpy import *
from PIL import Image

img = Image.open("enc.png")
image = array(img)			# store image data in numpy array
x, y, z = image.shape		# store image dimensions

flag = ''
# iterate through the 1st column only (coz all cols have same data)
for a in range(0, x):
	p = image[a,0]			# store pixel data
	
	# Brute-force chars in secret data
	for ch in range(256):	
		for k in range(256):
			r = ((k-10) * ch) % 251
			g = (k * ch) % 251
			b = ((k+10) * ch) % 251
			
			if r == p[0] and g == p[1] and b == p[2]:
				# print(k)
				flag += chr(ch)

print(flag)
