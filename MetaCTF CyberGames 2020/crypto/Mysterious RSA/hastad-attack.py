"""
author : MxRy - 2016 - Hastad's attack python2
https://github.com/MxRy/rsa-attacks/blob/master/hastad-attack.py
"""
import math
import functools
import gmpy2

# Get the Flag (only for CTFs)
def ReverseX(x, e) :
	m = gmpy2.iroot(x, e)[0]
	size = int(math.log(m, 10) + 1)
	print("Flag : \n"+"".join([chr((m >> j) & 0xff) for j in reversed(range(0, size << 3, 8))]))
	return 1	


# Step-by-step CRT implementation (cf. demo precedente)
def CrtComputation(C_i, N_i) :
	mu = list()
	nu = list()
	e = list()
	(x_i, N) = (0, 1)
	"""
	Calcul mu_i = PI_(j=1,j!=i)^k(n_j)
	"""
	N = functools.reduce(lambda a, b: a*b, N_i)
	for n_i in N_i :
		mu.append(N//n_i)
	"""
	Calcul nu_i inverse modulo n_i des mu_i
	useful link :
	https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
	"""
	for mu_i, n_i in zip(mu, N_i) :
		nu.append(gmpy2.invert(mu_i, n_i))
	"""
	Calcul e_i = nu_i * mu_i
	"""
	for mu_i, nu_i in zip(mu, nu) :
		e.append(mu_i*nu_i)
	"""
	Calcul et retour de x
	"""	
	for e_i, a_i in zip(e, C_i) :	
		x_i += e_i*a_i
	x = x_i % N
	return x 

def HastadAttack(C, N, e):
	x = CrtComputation(C, N)
	return ReverseX(x, e)

def main():	
	C = []
	N = []
	e = 0x43

	with open(" 0x43.txt", "r") as f:
		lines = f.read().split('\n')
		for i, line in enumerate(lines):
			if i <= e*2-1:
				if line[0] == 'N':
					N.append(int(line[3:], 16))
				else:
					C.append(int(line[3:], 16))
	HastadAttack(C, N, e)

if __name__ == "__main__":
	main()		
