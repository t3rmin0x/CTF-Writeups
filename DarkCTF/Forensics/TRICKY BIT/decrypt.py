with open("lsb1.bmp", "rb") as f:
	image = f.read()
	headless = image[54:]
	
	bin_str = ''
	for i in headless:
		current_char_binary = '{0:08b}'.format(i)	# convert current image byte to binary
		bin_str += str(current_char_binary)[-1:]	# extract the LSB from the current char binary

	hidden_text = ''
	hidden_text_size = 0
	DELIMITER = "$" 	
	for i in range(0, len(bin_str), 8):		
		eight_bits = bin_str[i:i+8]			# extract 8 bits from our binary string
		char = chr(int(eight_bits, 2))		# convert the binary back to char
		
		if(char == DELIMITER):					# DELIMITER helps us to get the length of hidden text
			hidden_text_size = int(hidden_text)		# get the length of the hidden text
			hidden_text = ''
		else:
			hidden_text += char
			# print(hidden_text)

		if(len(hidden_text) == hidden_text_size):
			print(hidden_text)
			break
