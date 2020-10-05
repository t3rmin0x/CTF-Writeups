# pip3 install python-levenshtein
# https://stackoverflow.com/questions/28172261/how-to-import-and-use-python-levenshtein-extension-on-osx
import Levenshtein as ls
import string

file = open("trainofthought.txt", "r").read().strip()
words = file.split(' ')

flag = ''
for i in range(len(words)-1):
	lev_dis = ls.distance(words[i], words[i+1])		# Levenshtein dist of 2 consecutive words
	alph = string.ascii_lowercase[lev_dis-1]		# lowercase alphabate mapping a = 1
	print("{} -> {}".format(lev_dis, alph))
	flag += alph		

print("flag{"+ flag  +"}")