# Totem 
> 100 Points 

# Description
> Is this a dream or not? Use your totem to find out. Flag format: ctf{}. <br>
> nc chal.ctf.b01lers.com 2008 <br>
> [totem-template.py](totem-template.py)

# Solution
We just have to implement the **cipher decoding algorithms** in python and modify the script.

### Script - [totem_solve.py](totem_solve.py)

```py
from pwn import *
import codecs
from base64 import b64decode
from string import ascii_lowercase

HOST = 'chal.ctf.b01lers.com'
PORT = 2008

r = remote(HOST,PORT)

# https://www.geeksforgeeks.org/baconian-cipher/
def bacon(s):
    # Do this
    pt = ''
    for i in range(0, len(s), 5):
        code = s[i:i+5]
        bin_code = code.replace('A', '0').replace('B', '1')
        int_code = int(bin_code, 2)
        ch = chr(97 + int_code)
        pt += ch        
    
    return pt

def rot13(s):
    # And this
    return codecs.decode(s, 'rot_13')

# https://exercism.io/tracks/python/exercises/atbash-cipher/solutions/2b513bc799984cc7aeb53513b81824d7
def atbash(s):
    # And this one
    plain = "abcdefghijklmnopqrstuvwxyz"
    cipher = "zyxwvutsrqponmlkjihgfedcba"

    pt = ''
    for x in s:
        pt += plain[cipher.index(x)]

    return pt

def Base64(s):
    # Lastly this one
    return base64.b64decode(s).decode()

if __name__ == '__main__':
    count = 0
    while True:     
        r.recvuntil('Method: ')
        method = r.recvuntil('\n').strip()
        r.recvuntil('Ciphertext: ')
        argument = r.recvuntil('\n').strip()

        result = globals()[method.decode()](argument.decode())  # :)
        # result = method(argument)

        r.recv()
        r.sendline(result.encode())
        count += 1
        if count == 1000:
            print(r.recv())
            exit(0)

        print("[+] Done >>> ", count)
    
```
# Flag
> ctf{4n_313g4nt_s01ut10n_f0r_tr4cking_r341ity}
