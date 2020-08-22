## Challenge: Irritate
> Obscurity is key for security
## Solution:
The file contains a big base64 string... so we decode it and find that another base64 string is formed. So I made a python script to solve it

```py
import os

c = 0
while(c<48):
	source = "/root/Documents/Phantom_CTF/Irritate/file" + str(c)
	output = "/root/Documents/Phantom_CTF/Irritate/file" + str(c+1)
	os.system("base64 -d "+source+" > "+output)
	c = c+1
```
## Flag:
>pCTF{1s_it_5t1ll_h4ck4ble}
