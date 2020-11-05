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

# CYCTF{latiniscool}