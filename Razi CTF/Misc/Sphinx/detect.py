from pwn import *
import base64
import cv2
import numpy as np
import collections

def pos(x, y, w, h):
	if x<=w//2 and y<=h//2:
		p = 'a' # top left
	elif x>w//2 and y<=h//2:
		p = 'b' # top right
	elif x<=w//2 and y>=h//2:
		p = 'c' # bottom left
	else:
		p = 'd' # bottom right
	return p

def name(a):
	if a==3:
		n = 'triangle'	# Triangle
	elif a==4:
		n = 'square'	# Square
	elif a==16:
		n = 'circle'	# Circle
	else:
		n = 'cross' # Cross
	return n

def detect(img, q):
	img = cv2.bitwise_not(img)
	
	h, w = img.shape
	
	_, threshold = cv2.threshold(img, 190, 255, cv2.THRESH_BINARY)
	contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	for cnt in range(1, len(contours)):
		approx = cv2.approxPolyDP(contours[cnt], 0.01*cv2.arcLength(contours[cnt], True), True)
		# cv2.drawContours(img, [approx], 0, (0), 5)

		x = approx.ravel()[0]
		y = approx.ravel()[1]

		shape = name(len(approx))
		posi = pos(x, y, w, h)
		# print(shape, posi)
		# print()
		if shape == q:
			# print(posi)
			return posi
	
	# cv2.imshow("shapes", img)
	# # cv2.imshow("Threshold", threshold)
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()

def main():
	# nc sphinx.razictf.ir 1379
	r = remote("sphinx.razictf.ir", 1379)

	# print(r.recv().decode())
	r.recv()
	r.sendline("yes")
	
	for i in range(20):
		data = r.recvuntil('\n')
		q = r.recv().decode().split(' ')[2]		# question
		print("[+] Searching  for: ", q)

		dec = base64.b64decode(data)
		file = open("shape.png", "wb").write(dec)
		img = cv2.imread("shape.png", cv2.IMREAD_GRAYSCALE)
		
		res = detect(img, q)
		print("Found pos: ", res)

		r.sendline(res.encode())
	
	r.interactive()
	
main()