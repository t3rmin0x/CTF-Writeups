# Hash Browns
> 400 points

## Description
> Thanks to your help, we have found evidence relating to the unF0r7un@t3s at the location you uncovered in in "(un)F0r7un@t3". We apprehended a couple subjects.
> It turns out they were planning something bigger, and that was only the beginning. We found a drive containing password-encrypted, and managed to find the 
> passwords hash, located in hash.txt below. We have reason to believe that the password starts with the name of a city (in lowercase) in France 
> (which is the country they attacked last), and ends with up to 7 numbers. For example: paris1337 (don’t try that that’s not the flag). Please decrypt the password.
> <br>[hash.txt](hash.txt)

## Solution
Looking at the hash we can assume that it's **SHA512**. So, I made a wordlist of all the cities in France from [this site](https://www.map-france.com/cities/) and
then I wrote a hash cracker in python and cracked the SHA512 hash.

### Script : [crack.py](crack.py)
```py
import hashlib

def check(passwd):
	orig_hash = 'F3899973D90D9EBB3A03ABC143B293CD33CFD688CB949AE1FBA61ACAB0D3D6220948AB3C35E00AF9D9497484B666D7FEA9D7673E2FC6AE463936C7B797FB3AF0'
	
	for i in range(9999999+1):
		s = passwd + str(i)
		new_hash = hashlib.sha512(s.encode()).hexdigest().upper()
		if new_hash == orig_hash:			
			return s
	return 0

cities = open('cities.txt','r').read().split('\n')
for city in cities:
	print(f"[+] Trying: {city.lower()}")	
	
	if check(city.lower()) != 0:		
		print(f"\n[+] Found: {check(city.lower())}")
		exit()

```
### Output:
```console
root@kali:~/Downloads/cyberyoddha/password_cracking# python3 crack.py 
[+] Trying: paris
[+] Trying: marseille
[+] Trying: lyon
[+] Trying: toulouse
[+] Trying: nice
[+] Trying: nantes
[+] Trying: strasbourg
[+] Trying: montpellier
[+] Trying: bordeaux
[+] Trying: lille
[+] Trying: rennes
[+] Trying: reims
[+] Trying: le havre
[+] Trying: saint-étienne
[+] Trying: toulon
[+] Trying: grenoble

[+] Found: grenoble38100
```

## Flag
> **CYCTF{grenoble38100}**
