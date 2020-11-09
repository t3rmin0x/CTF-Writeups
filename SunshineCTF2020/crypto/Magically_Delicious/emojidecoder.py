from itertools import *

cipher = "⭐🌈🍀 ⭐🌈🦄 ⭐🦄🌈 ⭐🎈🍀 ⭐🦄🌑 ⭐🌈🦄 ⭐🌑🍀 ⭐🦄🍀 ⭐🎈⭐ 🦄🦄 ⭐🦄🎈 ⭐🌑🍀 ⭐🌈🌑 ⭐🌑⭐ ⭐🦄🌑 🦄🦄 ⭐🌑🦄 ⭐🦄🌈 ⭐🌑🍀 ⭐🦄🎈 ⭐🌑🌑 ⭐🦄⭐ ⭐🦄🌈 ⭐🌑🎈 🦄🦄 ⭐🦄⭐ ⭐🌈🍀 🦄🦄 ⭐🌈🌑 ⭐🦄💜 ⭐🌑🦄 🦄🦄 ⭐🌑🐴 ⭐🌑🦄 ⭐🌈🍀 ⭐🌈🌑 🦄🦄 ⭐🌑🦄 ⭐🦄🌈 ⭐🌑🍀 ⭐🦄🎈 ⭐🌑🌑 ⭐🦄⭐ ⭐🦄🌈 ⭐🌑🎈 🦄🦄 ⭐🦄🦄 ⭐🌑🦄 ⭐🌈🌑 ⭐🦄💜 ⭐🦄🎈 ⭐🌑🌑 ⭐🎈🦄".split(' ')

"""
Brute-force these emojis for the correct octal code
🌑,💜,🐴 : (0,2,4)
"""

def breakit(emap):
	flag = ''
	for chunk in cipher:
		octcode = ''					
		for emoji in chunk:
			octcode += emap[emoji]
		flag += chr(int(octcode, 8))	# octal code to ASCII i.e., 163 = 's'
	print(flag)

def makeit():
	emomap = {
	'⭐' : '1',
	'🌈' : '6',
	'🍀' : '3',
	'🦄' : '5',
	'🎈' : '7'
	}

	# permutations of emoji and relative numbers
	numperms = permutations(['0','2','4'])
	emo = ['🌑','💜','🐴']

	for nums in numperms:
		temp = {}
		for i in range(len(nums)):
			temp[emo[i]]=nums[i]
		emomap.update(temp)
		# try to break it with every possible emoji-maps
		breakit(emomap)

if __name__ == '__main__':
	makeit()