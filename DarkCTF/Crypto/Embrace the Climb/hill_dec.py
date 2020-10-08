#!/usr/bin/env python3
import numpy as np
from sympy import *
import itertools

def make_char_set():
    init = "abcdefghijklmnopqrstuvwxyz0123456789"
    end = "{}_ "
    char_set = []
    
    comb = list(itertools.permutations(end, 4))     # rearranges end characters i.e. "{}_ "
    for i in range(len(comb)):
        end = ''.join(c for c in comb[i])
        char_set.append(init + end)
    return char_set

def decrypt(ciphertext, key, char_set):
    key = Matrix(key)
    # Calculate inverse of the Key matrix(mod N) where N = no. of chars in alphabet
    inv_key = key.inv_mod(40)       

    pt = ''
    # Loop through n chars at a time when Key matrix is n x n
    for i in range(0, len(ciphertext), 3):
        chars = ciphertext[i : i+3]     
        chars_index = [char_set.index(ch) for ch in chars] 
        res = np.dot(inv_key, chars_index) % 40         # matrix mult and (mod N)
        pt += ''.join(char_set[int(i)] for i in res)
    return pt

ciphertext = "lkeitrx66dcw{3zy1}tvzlrb4ilp9}1m0ifqjvuu3 1m0h9b5dc ucu3eicw{n}nauu3 95o00jd 0q55x66nwm"
key = [ [6, 24, 1],         # key matrix
        [13, 16, 10], 
        [20, 17, 15]
    ]       

char_set = make_char_set()     # make a list of possible character set (alphabet)

for x in char_set:
    print("[*] Decrypted with char_set : " + x)
    print(">>>", decrypt(ciphertext, key, x), "\n")