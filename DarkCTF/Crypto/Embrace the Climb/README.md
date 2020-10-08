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

```py
#!/usr/bin/env python3
import numpy as np
from sympy import *
import itertools

def make_char_set():
    init = "abcdefghijklmnopqrstuvwxyz0123456789"
    end = "{}_ "
    char_set = []
    
    comb = list(itertools.permutations(end, 4))     # rearranges end characters i.e. "{}_ "
    for i in range(len(comb)):
        end = ''.join(c for c in comb[i])
        char_set.append(init + end)
    return char_set

def decrypt(ciphertext, key, char_set):
    key = Matrix(key)
    # Calculate inverse of the Key matrix(mod N) where N = no. of chars in alphabet
    inv_key = key.inv_mod(40)       

    pt = ''
    # Loop through n chars at a time when Key matrix is n x n
    for i in range(0, len(ciphertext), 3):
        chars = ciphertext[i : i+3]     
        chars_index = [char_set.index(ch) for ch in chars] 
        res = np.dot(inv_key, chars_index) % 40         # matrix mult and (mod N)
        pt += ''.join(char_set[int(i)] for i in res)
    return pt

ciphertext = "lkeitrx66dcw{3zy1}tvzlrb4ilp9}1m0ifqjvuu3 1m0h9b5dc ucu3eicw{n}nauu3 95o00jd 0q55x66nwm"
key = [ [6, 24, 1],         # key matrix
        [13, 16, 10], 
        [20, 17, 15]
    ]       

char_set = make_char_set()     # make a list of possible character set (alphabet)

for x in char_set:
    print("[*] Decrypted with char_set : " + x)
    print(">>>", decrypt(ciphertext, key, x), "\n")
    
```
### Script - [hill_dec.py](hill_dec.py)

### Output
```bash
┌──(root 🔱 r3yc0n1c)-[/darkCTF-finals/crypto/Embrace the Climb]
└─# ./hill_dec.py
[*] Decrypted with char_set : abcdefghijklmnopqrstuvwxyz0123456789{}_ 
>>> {h1ll_cl1mb1n9_15_h4rd_bu7_n07_7h3_c1ph3r__7h3_b357_v13w_c0m35_4f73r_7h3_h4rd357_cl1mb} 

[*] Decrypted with char_set : abcdefghijklmnopqrstuvwxyz0123456789{} _
>>> {h1ll cl1mb1n9 15 h4rd bu7 n07 7h3 c1phfyo 7h3 b357iqg3w c0m35 4f7fyo7h3 h4anl57 cl1mb} 

[*] Decrypted with char_set : abcdefghijklmnopqrstuvwxyz0123456789{_} 
>>> {h1ll}cl1mb1n9}lywh4rd}bu7}_tr}7h3}c1ph3r}}7h3}b357}v13w}c0mnyw4f73r}7h3}h4rd357}cl1mb_ 

[*] Decrypted with char_set : abcdefghijklmnopqrstuvwxyz0123456789{_ }
>>> {h1ll cl1mb1n9 9rgh4rd bu7 vmb 7h3 c1phfyo 7h3 b357iqg3w c0m_rg4f7fyo7h3 h4anl57 cl1mb_ 

[*] Decrypted with char_set : abcdefghijklmnopqrstuvwxyz0123456789{ }_
>>> {h1ll}cl1mb1n9}lywh4rd}bu7} tr}7h3}c1phv54}7h3}b357slz3w}c0mnyw4f7v547h3}h4xx757}cl1mb 

...

```
## Flag 
> darkCTF{h1ll_cl1mb1n9_15_h4rd_bu7_n07_7h3_c1ph3r__7h3_b357_v13w_c0m35_4f73r_7h3_h4rd357_cl1mb}

### Read about it here :
* [Hill cipher - Wikipedia](https://en.wikipedia.org/wiki/Hill_cipher)
* [Hill Cipher - Crypto Corner](https://crypto.interactive-maths.com/hill-cipher.html)
