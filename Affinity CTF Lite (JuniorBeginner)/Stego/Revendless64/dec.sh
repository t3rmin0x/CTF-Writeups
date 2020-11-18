#!/bin/bash -e
c=0
while true
do
	f=$(cat z | rev | base64 -d)
	echo $f > z
	c=$(($c+1))
	echo "mission $c passed!"
	echo "    Respect +"
done