# Train of Thought
> 100 Points 

# Description
> We've managed to infiltrate Mr. Levenshtein's subconscious, but he keeps losing his train of thought! Sort out the noise and find the flag in this mess. <br>
> Wrap the decrypted string in flag{xxxxxxxxx} for submission <br>
> [trainofthought.txt](trainofthought.txt)

# Solution
After trying different approaches (failed in all of them and almost gonna giveup `;-;`), I decided to read the description again and search for the word **Levenshtein**. 

The search result showed - [Levenshtein distance - Wikipedia](https://en.wikipedia.org/wiki/Levenshtein_distance)

Then I thought the words look ~similar~, I mean we can add, remove or replace letters to transform them into one another. 
Umm... maybe we can calculate the **Levenshtein Distance** of the consecutive words (random guess, 1st I tried to calculate 2 words at a time `:p`).

I searched a little more and got hind that we can map these **Levenshtein Distances** with the letters in english alphabet. A simple python script did the job and 
I got the flag. `\(^-^)/`

### Script - [leven.py](leven.py)

```py
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
```
# Flag
> flag{anorganizedmind}
