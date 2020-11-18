# Revendless64
> Points 30
> Solved by r3yc0n1c

## Description
> :arrow_down: [z.7z](z.7z)

# Solution
General analysis showed that the file has only `1` word with `68340085` bytes (WTF!!!)
```zsh
┌──(root 🌀 kali)-[~/Downloads/affinityCTF/steg/how_many_times_I_need_to_do_base64?]
└─# file z   
z: ASCII text, with very long lines, with no line terminators

┌──(root 🌀 kali)-[~/Downloads/affinityCTF/steg/how_many_times_I_need_to_do_base64?]
└─# wc -wc z
       1 68340085 z
                                                                                                                                                                                              
┌──(root 🌀 kali)-[~/Downloads/affinityCTF/steg/how_many_times_I_need_to_do_base64?]
└─# xxd -l 200 z   
00000000: 3d3d 6743 5442 5452 345a 6c61 5770 5559  ==gCTBTR4ZlaWpUY
00000010: 786f 4657 5870 6d52 5446 4752 4752 5856  xoFWXpmRTFGRGRXV
00000020: 7849 3153 5731 6d53 7a51 5662 3464 6c55  xI1SW1mSzQVb4dlU
00000030: 3678 4753 615a 4663 764a 5662 4768 6b55  6xGSaZFcvJVbGhkU
00000040: 7252 5761 574e 5451 3664 5656 6f39 3256  rRWaWNTQ6dVVo92V
00000050: 4770 4657 6b64 554d 555a 4662 4b64 5557  GpFWkdUMUZFbKdUW
00000060: 7452 484d 695a 6c56 3656 3161 6b5a 5657  tRHMiZlV6V1akZVW
00000070: 584a 6c56 5578 4761 684a 3252 5768 3156  XJlVUxGahJ2RWh1V
00000080: 7468 3356 6b46 6a56 3259 4662 4f52 6a55  th3VkFjV2YFbORjU
00000090: 7930 6b4d 5674 6d57 7046 474d 3163 3056  y0kMVtmWpFGM1c0V
000000a0: 754a 3162 585a 455a 594a 5662 7768 6c56  uJ1bXZEZYJVbwhlV
000000b0: 455a 6b56 5556 4664 4464 6c52 776c 6b55  EZkVUVFdDdlRwlkU
000000c0: 724a 4657 695a 6b57                      rJFWiZkW

```
But the data seems to be mutiple time base64 encoded (the unzipped folder hinted that) but the padding is weird! So I thought maybe the string is reversed 
and thus wrote a script to solve it.
### Script - [decode.py](decode.py)
```py
import base64

with open('z') as f:
	data = f.read().strip()
	i = 0	
	while True:	
		try:
			data = data[::-1]
			print(f"STARTING LVL {i}")
			new = base64.b64decode(data)
			data = new.strip()
			print(f"DONE LVL {i}")
		except:
			print(new)
			break
		i = i+1
```
## Flag
> **AFFCTF{s1mPle_Rev4s_D0Ne_oNe1}**

## Bash is more powerful than you think!
My bash approach was relatively slower and I tried it as an experiment.
### Script - [dec.sh](dec.sh)
```zsh
#!/bin/bash -e
c=0
while true
do
	f=$(cat z | rev | base64 -d)
	echo $f > z
	c=$(($c+1))
	echo "mission $c passed!"
	echo "    Respect +"
done
```
```zsh
┌──(root 🌀 kali)-[~/Downloads/affinityCTF/steg/how_many_times_I_need_to_do_base64?]
└─# ./dec.sh 
mission 1 passed!
    Respect +
mission 2 passed!
    Respect +
mission 3 passed!
    Respect +
...
...
...
mission 49 passed!
    Respect +
mission 50 passed!
    Respect +
base64: invalid input
                                                                                                                                                                                              
┌──(root 🌀 kali)-[~/Downloads/affinityCTF/steg/how_many_times_I_need_to_do_base64?]
└─# cat z                                                                                                                                                                                 1 ⨯
AFFCTF{s1mPle_Rev4s_D0Ne_oNe1}
```
