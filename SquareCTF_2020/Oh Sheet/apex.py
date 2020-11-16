import string
from itertools import *
import re

def keygen(cipher):
    print("\n[+] Generating keyspace...\n")
    
    alpha = string.ascii_lowercase		# [a-z]
    cmap = alpha*2						# character map
    newkeys = []

    # Brute-force [a-z] and find chars that satisfy the conitions
    for c1 in cipher:
        char = []
        for c2 in alpha:
            l = chr(c1 - ord(c2))
            if l==' ':				# plaintext may contain space(' ')
                char.append(c2)
            try:
                # $E$80 = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
                # =FIND(L81, $E$80) - FIND(E81, $E$80)
                m = cmap.index(l) - cmap.index(c2)
                # =FIND(L81, $E$80, FIND(L81, $E$80)+1) - FIND(E81, $E$80)
                n = cmap.rindex(l) - cmap.index(c2)
                # =FIND(L81, $E$80, FIND(L81, $E$80)+1) - FIND(E81, $E$80, FIND(E81, $E$80) + 1)
                o = cmap.rindex(l) - cmap.rindex(c2)
                # =MIN(FILTER(M83:O83, M83:O83 > 0))
                p = min([i for i in [m,n,o] if i>0])
                err = cmap[p-1]   
                char.append(c2)             
                # print(c2,ord(c2),chr(c1),c1,ord(l),l,m,n,o,p,decoded)
            except:
                pass
        newkeys.append(char)

    final = newkeys[:9]		# first 9 letters are fine coz original key_length is 9 final key is repeated
    # pure guess
    # final[0] = ['j','f']
    # final[1] = ['q']
    # final[6] = ['c']
    # for i in range(2,9):
    # 	if i != 6:
    # 		if 'j' in final[i]:
    # 			final[i].remove('j')
    # 		if 'f' in final[i]:
    # 			final[i].remove('f')
    # 		if 'c' in final[i]:
    # 			final[i].remove('c')
    # 		if 'q' in final[i]:
    # 			final[i].remove('q')
    
    for k in final:
        print(k)
    
    print("\n[+] Starting Brute-force...")
    perms = product(*final)					# store all key combos
    for p in perms:
        p = ''.join(p)
        chk = True
        for ch in p:
            if p.count(ch)>1:		# check for repeating key chars
                chk = False
                break
        if chk:
            decrypt(cipher, p, cmap)

def decrypt(cipher, key, cmap):
	# Orig key = 'squarectf'
	rep_key = list(islice(cycle(key),19))	# cyclic repeat key
	decoded = ''
	for c1,c2 in zip(cipher, rep_key):
		l = chr(c1 - ord(c2))
		if l==' ':
			decoded += l
		try:
			# $E$80 = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
			# =FIND(L81, $E$80) - FIND(E81, $E$80)
			m = cmap.index(l) - cmap.index(c2)
			# =FIND(L81, $E$80, FIND(L81, $E$80)+1) - FIND(E81, $E$80)
			n = cmap.rindex(l) - cmap.index(c2)
			# =FIND(L81, $E$80, FIND(L81, $E$80)+1) - FIND(E81, $E$80, FIND(E81, $E$80) + 1)
			o = cmap.rindex(l) - cmap.rindex(c2)
			# =MIN(FILTER(M83:O83, M83:O83 > 0))
			p = min([i for i in [m,n,o] if i>0])
			decoded += cmap[p-1]
			# print(c2,ord(c2),chr(c1),c1,ord(l),l,m,n,o,p,cmap[p-1])
		except:
			pass

	if len(decoded) == 19:
		print(f"{key} -> {decoded} -> {len(decoded)}")


def main():
	cipher = [213,145,220,209,224,207,131,235,222,229,216,228,209,235,220,199,222,212,229]
	keygen(cipher)

if __name__ == "__main__":
	main()
