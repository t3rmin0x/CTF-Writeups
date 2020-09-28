# haxXor
> Points: 281

## Description
> you either know it or not take this and get your flag

`5552415c2b3525105a4657071b3e0b5f494b034515`
## Solution
I did a XOR brute force first in [CyberChef](https://gchq.github.io/CyberChef/) but nothing useful came out. 

So I tried a partial plain text attack.

I knew the start of the flag was **darkCTF{** (partial plain text) so I xored it with the given hexvalue to get the `key`.

Once I got the key I padded it to match the length of the cipher. Finally I xored the padded key and cipher to get the flag.

```py
#!/bin/env python3

hex_string = "5552415c2b3525105a4657071b3e0b5f494b034515"
flag = b'darkCTF{'

key = []
f = []

#finding the secret key
b = bytes.fromhex(hex_string)	
for c, m in zip(b, flag):
	key.append(chr(c ^ m))
print("Secret key : " + ''.join(key))

#using the secret key to decrypt 
secret = b'1337hack1337hack1337h'

for c, m in zip(b, secret):
	f.append(chr(c ^ m))
final_flag = ''.join(f)
print("Final flag is : " + final_flag)
```

## Flag
> darkCTF{kud0s_h4xx0r}
