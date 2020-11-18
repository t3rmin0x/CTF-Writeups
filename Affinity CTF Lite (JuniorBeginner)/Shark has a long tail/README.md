# Shark has a long tail
> Points: 663

## Desc
> We intercept the attack traffic and we know that there is a message in packets encoded in some tricky way. Can you help us decode it.<br>
> :arrow_down: [SharkHasALongTail.pcap](SharkHasALongTail.pcap)

## Sol
### Script - [getflag.py](getflag.py)
```py
#!/usr/bin/env python3
import os

os.system("tshark -r SharkHasALongTail.pcap -T fields -e tcp.len > out.txt")
print("tshark is closed!\nFinal output:\n")
out = open("out.txt").read().strip().split('\n')
print(''.join(chr(int(c)) for c in out))

```
## Flag
> **AFFCTF{TCPDUMP_Never_Disappoints}**
