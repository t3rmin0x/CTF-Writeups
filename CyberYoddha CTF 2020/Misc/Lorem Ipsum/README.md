# Lorem Ipsum
> 125 points

## Description
> Lorem ipsum dolorc sit amet, consectetury adipiscing celit, sed dot eiusmod tempor incifdidunt ut labore et dolore magna aliqual. Ut enim ad minima veniam, 
> quist nostrud exercitation ullamcoi laboris nisin ut aliquip ex eai commodos consequat. Duis caute irure dolor in reprehenderit in voluptate velit oesse 
> cillum dolore eu fugiat nulla pariatur. Excepteur osint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim lid est laborum.

## Solution
A quick comparison of [this text](cipher.txt) with the [default](orig.txt) ***Lorem Ipsum*** paragraph gives us the flag.

### Script: [check.py](check.py)
```py
orig = open("orig.txt", 'r').read().split(' ')
cipher = open("cipher.txt", 'r').read().split(' ')

assert len(orig) == len(cipher)

flag = ''
for w1, w2 in zip(orig, cipher):
	print(w1, w2)
	w1 = list(w1)
	for ch in w2:
		if ch not in w1:
			flag += ch
		else:
			w1.remove(ch)

print(f"\nFlag:\n{flag}")

```
## Flag
> **CYCTF{latiniscool}**
