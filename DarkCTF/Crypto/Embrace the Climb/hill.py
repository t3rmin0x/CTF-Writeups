import math
import sympy
from sympy import init_printing, pprint
from sympy import Matrix
from sympy.vector import matrix_to_vector, CoordSysCartesian
init_printing()

def decrypt(matrix, words, alph_map):
    cipher = ''
    M = Matrix(matrix)
    M = M.inv_mod(40)	# inverse of the matrix M (mod N) (where N = no. of letters in alphabate)
    length = len(M)
    d = {}
    d2 = {}
    
    alph = alph_map

    for x in range(len(alph)):
        d[alph[x]] = x
        d2[x] = alph[x]
    
    count = 0
    l = []

    for ch in words:
        if (count+1) % (3+1) == 0:
            m = Matrix(l)
            dot_pr_m = M*m
            
            n = []
            for i in dot_pr_m:
                cipher += d2[i % 40]
            count = 0
            l = []
        l.append(d[ch])
        count += 1
    if (count+1) % (3+1) == 0:
        m = Matrix(l)
        dot_pr_m = M*m
        
        n = []
        for i in dot_pr_m:
            cipher += d2[i % 40]
    return cipher

if __name__ == '__main__':
    
    secret = [[6,24,1], [13,16,10], [20,17,15]]		# key matrix
    ciphertext = "lkeitrx66dcw{3zy1}tvzlrb4ilp9}1m0ifqjvuu3 1m0h9b5dc ucu3eicw{n}nauu3 95o00jd 0q55x66nwm"
    
    print("[+] CipherText: \n"+ ciphertext)

alph_maps = ["abcdefghijklmnopqrstuvwxyz0123456789_{} ",
			"abcdefghijklmnopqrstuvwxyz0123456789 {}_",
			"abcdefghijklmnopqrstuvwxyz0123456789 {_}",
			"abcdefghijklmnopqrstuvwxyz0123456789_{ }",
			"abcdefghijklmnopqrstuvwxyz0123456789{} _"
			]

print("[+] PlainText : \n")
for alph_map in alph_maps:
	print(decrypt(secret, ciphertext, alph_map))
