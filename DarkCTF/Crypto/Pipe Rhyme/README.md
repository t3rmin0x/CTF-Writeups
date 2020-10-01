# Pipe Rhyme
> Points: 249
## Description
> So special
>
>[File](https://mega.nz/file/jwUWnDID#qtXnMNkjeTzw-2ESH1xOat5sGoosMbBpIUGClq8xOyY)

## Solution
This was a simple RSA. I used [factordb](http://factordb.com/index.php?id=1100000001575896728) to factorise the modulo value `N` and found `p` and `q`.

Here's the script:
```py
#!/bin/env python3

import gmpy
from Crypto.Util.number import long_to_bytes

N="0x3b7c97ceb5f01f8d2095578d561cad0f22bf0e9c94eb35a9c41028247a201a6db95f"
e=0x10001
ct="0x1B5358AD42B79E0471A9A8C84F5F8B947BA9CB996FA37B044F81E400F883A309B886"

N = int(N,16)
ct = int(ct,16)

p = 31415926535897932384626433832795028841
q = 56129192858827520816193436882886842322337671
phi = (p-1)*(q-1)
d = gmpy.invert(e,phi)

pt = long_to_bytes(pow(ct,d,N)).decode()
print("Flag is : " + str(pt))
```
## Flag
>darkCTF{4v0iD_us1ngg_p1_pr1mes}
