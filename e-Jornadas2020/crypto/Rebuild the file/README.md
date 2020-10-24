# Rebuild the file
> 300 pts

# Desc
> Find the magic file hidden under ctf.flagsource.tk. <br>
> Flag format: flag{string}

# Sol

```py
import subprocess
import re

d = ''

with open("file.txt", "w") as f:
	try:
		i = 1
		while True:
			print(f"Got Part [{i}]")
			proc = ["dig","ANY","@summer2020.ctf.cert.rcts.pt","part" +str(i)+ ".file.ctf.flagsource.tk"]
			recv = subprocess.Popen(proc, stdout=subprocess.PIPE).communicate()[0].decode()

			data = re.search('"(.+?)"', recv).group(1)	# regex find the hex bytes
			f.write(data)
			i += 1
			d += data
	except:
		print("\nDONE!!!")

# test file.txt and save
with open("flag.bmp", "wb") as f:
	f.write(bytes.fromhex(d))

```
### Output: [file.txt](file.txt)

![flag](flag.bmp)

## Flag
> flag{m@g1c_byt3s}
