from PIL import Image

img = Image.open('image.png')
data = img.getdata()

bindata = ''
for p in data:
	# convert black pixels to 1 and white to 0
	bindata += '1' if p[0]==0 else '0'
print(bindata)

assert len(bindata)%8 == 0

# decode binary data
flag = ''
for i in range(0, len(bindata), 8):
	chunk = bindata[i : i+8]
	flag += chr(int(chunk, 2))
print(flag)
