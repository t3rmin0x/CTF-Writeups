# Embrace the Climb ![badge](https://img.shields.io/badge/Post%20CTF-Writeup-success)
> Points: 497

## Description
> Gaining altitude ...  <br>
> lkeitrx66dcw{3zy1}tvzlrb4ilp9}1m0ifqjvuu3 1m0h9b5dc ucu3eicw{n}nauu3 95o00jd 0q55x66nwm   <br>
> \> 6  24 1   <br>
> \> 13 16 10  <br>
> \> 20 17 15  <br>

## Solution
We can get a hint from the Description and the name of the Challenge that it is **Hill Cipher**.

**The basic idea behind the Encryption Scheme is :**
* Select alphabate containting ***N*** letters.

| Letter |a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z|0|1|2|3|4|5|6|7|8|9|{|}| |_|
|--------|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
| Number |0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25|26|27|28|29|30|31|32|33|34|35|36|37|38|39|40|

* Use an ***n* x *n* invertible matrix (modulo *N*)** (where ***N*** is the total number of letters in the alphabate) as the key.
* Multiply each block of ***n*** plaintext letter numbers mapped to the respective letters with it.

**The Decryption Scheme is :**
* Select the same alphabate containting ***N*** letters. (In this challenge we have to guess the alphabate map from the ciphertext)
* Find the **inverse** of the given key matrix.
* Use the inverted ***n* x *n* matrix (modulo *N*)** as the key.
* Multiply each block of ***n*** ciphertext letter numbers mapped to the respective letters with it.

Luckily I found a script from an old writeup on similar challenge - [IceCTF [Cryptography] - Hill Cipher](https://teamrocketist.github.io/2016/08/26/IceCTF-Cryptography-Hill-Cipher/)
and I modified the script to find the flag.

```py
import math
import sympy
from sympy import init_printing, pprint
from sympy import Matrix
from sympy.vector import matrix_to_vector, CoordSysCartesian
init_printing()

def decrypt(matrix, words, alph_map):
    cipher = ''
    M = Matrix(matrix)
    M = M.inv_mod(40)	# inverse of the matrix M (mod N) (where N = no. of letters in alphabate)
    length = len(M)
    d = {}
    d2 = {}
    
    alph = alph_map

    for x in range(len(alph)):
        d[alph[x]] = x
        d2[x] = alph[x]
    
    count = 0
    l = []

    for ch in words:
        if (count+1) % (3+1) == 0:
            m = Matrix(l)
            dot_pr_m = M*m
            
            n = []
            for i in dot_pr_m:
                cipher += d2[i % 40]
            count = 0
            l = []
        l.append(d[ch])
        count += 1
    if (count+1) % (3+1) == 0:
        m = Matrix(l)
        dot_pr_m = M*m
        
        n = []
        for i in dot_pr_m:
            cipher += d2[i % 40]
    return cipher

if __name__ == '__main__':
    
    secret = [[6,24,1], [13,16,10], [20,17,15]]		# key matrix
    ciphertext = "lkeitrx66dcw{3zy1}tvzlrb4ilp9}1m0ifqjvuu3 1m0h9b5dc ucu3eicw{n}nauu3 95o00jd 0q55x66nwm"
    
    print("[+] CipherText: \n"+ ciphertext)

alph_maps = ["abcdefghijklmnopqrstuvwxyz0123456789_{} ",
			"abcdefghijklmnopqrstuvwxyz0123456789 {}_",
			"abcdefghijklmnopqrstuvwxyz0123456789 {_}",
			"abcdefghijklmnopqrstuvwxyz0123456789_{ }",
			"abcdefghijklmnopqrstuvwxyz0123456789{} _"
			]

print("[+] PlainText : \n")
for alph_map in alph_maps:
	print(decrypt(secret, ciphertext, alph_map))

```
### Script - [hill.py](hill.py)

### Output
```bash
┌──(root 🔱 r3yc0n1c)-[/darkCTF-finals/crypto/Embrace the Climb]
└─# python3 hill.py                                                        
[+] CipherText: 
lkeitrx66dcw{3zy1}tvzlrb4ilp9}1m0ifqjvuu3 1m0h9b5dc ucu3eicw{n}nauu3 95o00jd 0q55x66nwm
[+] PlainText : 

_h1ll}cl1mb1datlywh4rd}bu7}{tr}7h3}c1ph3r}}7h3}b357}v13w}c0md3d4f73r}7h3}h4rd357}cl1mb{
 h1ll}cl1mb1datlywh4rd}bu7}{tr}7h3}c1ph{}g}7h3}b3572ge3w}c0md3d4f7{}g7h3}h4g7p57}cl1mb{
 h1ll_cl1mb1dat9rgh4rd_bu7_vmb_7h3_c1ph{_g_7h3_b3572ge3w_c0m1w14f7{_g7h3_h4g7p57_cl1mb{
_h1ll cl1mb1dat9rgh4rd bu7 vmb 7h3 c1phfyo 7h3 b357iqg3w c0m1w14f7fyo7h3 h4anl57 cl1mb{
{h1ll cl1mb1n9 15 h4rd bu7 n07 7h3 c1phfyo 7h3 b357iqg3w c0m35 4f7fyo7h3 h4anl57 cl1mb}

```
## Flag 
> darkCTF{h1ll_cl1mb1n9_15_h4rd_bu7_n07_7h3_c1ph3r__7h3_b357_v13w_c0m35_4f73r_7h3_h4rd357_cl1mb}

### Read about it here :
* [Hill cipher - Wikipedia](https://en.wikipedia.org/wiki/Hill_cipher)
* [Hill Cipher - Crypto Corner](https://crypto.interactive-maths.com/hill-cipher.html)
