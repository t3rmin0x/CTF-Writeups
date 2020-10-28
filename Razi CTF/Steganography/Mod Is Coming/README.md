# Mod Is Coming
> 986 points

## Description
> It's actually pretty simple when you think about it. <br>
> [File](Mod_Is_Coming.zip)

## Solution
This was a really cool challenge. We have an image file (`enc.png`) and a python script (`script.py`) which wass used to hide the **secret data** in the image.

### Analysis of the python script:

```py
import random
from numpy import *
from PIL import Image
from functools import reduce


def f1(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * f3(p, n_i) * p
    return sum % prod

# GCD
def f2(a, b): 
    if b == 0: 
        return a 
    else: 
        return f2(b, a%b) 

# Modular multiplicative inverse
def f3(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


def encrypt(s):
    c_p = []
    for i in range(10,21):
        for j in range(i+1,21):
            if f2(i,j) == 1:
                c_p.append([i,j])
    rand = random.randint(0,len(c_p))       # choose random integer
    k = f1(c_p[rand], [len(s), len(s)*3])   # generate random key
    while k == 0:
        rand = random.randint(0,len(c_p))
        k = f1(c_p[rand], [len(s), len(s)*3])
    img = Image.new('RGB', (len(s)*3, len(s)), color = 'white')   # create new image
    image = array(img)              # store image data in numpy array
    x, y, z = image.shape           # store image dimensions
    for a in range (0, x):
        for b in range (0, y):
            p = image[a, b]         # pixel data at co. (a, b)
            
            # hide secret data in the pixel values
            p[0] = ((k-10) * ord(s[a])) % 251      
            p[1] = (k * ord(s[a])) % 251           
            p[2] = ((k+10) * ord(s[a])) % 251      
            image[a][b] = p         # new image data
    enc = Image.fromarray(image)    # create image from new data
    enc.save('enc.png')

f = open("secretmsg.txt", "r")
encrypt(f.read())
```

I told my teammates about the analysis and we came up with the idea to brute-force the chars. ( These guys are amazing tbh :p )

### The solution [script](decoder.py):
```py
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
	for ch in range(ord('!'), ord('~')):	
		for k in range(256):
			r = ((k-10) * ch) % 251
			g = (k * ch) % 251
			b = ((k+10) * ch) % 251
			
			if r == p[0] and g == p[1] and b == p[2]:
				# print(k)
				flag += chr(ch)

print(flag)
```
### Output:
```sh
root@kali:~/Downloads/razi/steg/Mod Is Coming# python3 decoder.py 
Chaosisn'tapit.Chaosisaladder,Manywhotrytoclimbitfail,andnevergettotryagain,thefallbreaksthem.Andsomearegivenachancetoclimb,buttheyrefuse.Theyclingtotherealm,orthegods,orlove...illusions.Onlytheladderisreal,theclimbisallthereis.RaziCTF{7h3_script_1s_d4rk_4nd_full_0f_m0ds}
```

## Flag
> **RaziCTF{7h3_script_1s_d4rk_4nd_full_0f_m0ds}**

