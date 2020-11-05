#!/usr/bin/env python3
# https://metaproblems.com/8b2797bf7f420d5ad92e60ba064a55a1/index.php

import requests as r
import re

file = open('data.txt', 'w')
for i in range(1000):
	res = r.get("https://metaproblems.com/8b2797bf7f420d5ad92e60ba064a55a1/index.php").text
	stripped = re.sub('<[^<]+?>', '', res).split('\n\n')	# regex to get only N, E, C
	print(f"Collected {i+1}")

	n = stripped[0]
	e = stripped[1]
	ct = stripped[2]

	# store the N, C pairs in diff files with filename E
	with open(e[2:]+'.txt', 'a') as f:
		f.writelines(n+'\n'+ct)


