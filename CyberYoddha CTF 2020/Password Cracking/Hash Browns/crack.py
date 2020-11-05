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
