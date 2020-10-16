# Time to Coding
> 200 points

## Description
> Take a look at the python code file, and find the secret message in the file data.enc. <br>
> Flag format: flag{string} <br>
> :arrow_down: [data.enc](data.enc) :arrow_down: [encrypt.py](encrypt.py)

## Solution
There's a simple encryption function which we have to solve to decrypt the data in the **`data.enc`** file.

The encrypt function:
```py
def encrypt(data): 
    encrypted=""
    key=0x2F          # A random key 
    pre_enc=""
    for x in data:
        tmp = ord(x) 
        tmp = tmp ^ key     # each char in data is XORed with the key
        pre_enc+=chr(tmp)

    pre_enc=base64.b64encode(pre_enc)     # base64 encode the XORed data
    encrypted_data="" 
    for x in range(0, len(pre_enc)):   
        tmp = pre_enc[ len(pre_enc) - 1 -x ]    # stores each char of the pre_enc data in a reverse order
        encrypted_data+= chr(ord(tmp) + 5 )     # final encryption is done by increasing the ASCII value of each char by 5
           
    return encrypted_data
```
I wrote a simple python script to decrypt it.
### Script - [decrypt.py](decrypt.py)
```py
import base64

def decrypt(data):
    pre_dec = ''
    for x in range(len(data)):
        tmp = data[len(data) - 1 - x]
        pre_dec += chr(ord(tmp) - 5)
    
    pre_dec = base64.b64decode(pre_dec.encode())
    
    key = 0x2F
    decrypted = ''
    for x in pre_dec:
        decrypted += chr(x ^ key)

    return decrypted

ct = open("data.enc", 'r').read()
print(decrypt(ct))
```

## Flag
> flag{Th1S_is_N0t_safe}
