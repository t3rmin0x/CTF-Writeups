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