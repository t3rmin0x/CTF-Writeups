# Shared Dreaming
> 100 Points 

# Description
> It's not just about depth you know, you need the simplest version of the idea in order for it to grow naturally in a subject's mind; it's a very subtle art. <br>
> [shareddreaming.txt](shareddreaming.txt)

# Solution
From the **Hints** in the given flie, we can calculate **`flag ⊕ RandByte`** and then we can simply do a **XOR Known Plain Text Attack (KPA)** to 
find the flag. 

### Script - [exploit.py](exploit.py)

```py
#!/bin/env python3

def KPA(ct):	
	known = ord('f') 		# from flag format = known byte
	pad = ct[0] ^ known		# 1st byte ^ known byte

	pt = ''
	for ch in ct:
		pt += chr(pad ^ ch)
	return pt

a1a2a3a4 = 0x8ba4c4dfce33fd6101cf5c56997531c024a10f1dc323eb7fe3841ac389747fb90e3418f90011ef2610fa3636cd6cf0002d19faa30d39161fbd45cc58abff6a84
a2a3a4 = 0xf969375145322aba697ce9b4e00aa88e81ffe5c306b1b98148f33c4581b2ac39bc95f13b27c39f2311a590b7e27cdbdb7599f615acd70c45378e44fb319b8cb6
a1a3 = 0x855249b385f7b1d9923f71feb3bdee1032963ab51aa7b9d89a20c08c381e77890aa8849702d8791f8e636e833928ba6ea44c5f261983b7e29bd82e44b77fe03b
flaga3Rb = 0xf694bc3d12a0673aead8fc4fdf964f5ec0c1d938e722bf333000f300088ead0dec1e7e03720331098068c13a066ca9bca89850a8ee67feb8471af5f47b4c0f13

a1 = a1a2a3a4 ^ a2a3a4
a3 = a1 ^ a1a3
flagRb = flaga3Rb ^ a3

ct = '0' + str(hex(flagRb))[2:]		# padding is important
pt = KPA(bytearray.fromhex(ct))

print(pt)
```

# Flag
> flag{1f_w3_4r3_g0nn4_p3rf0rm_1nc3pt10n_th3n_w3_n33d_1m4g1n4t10n}
