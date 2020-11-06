#!/bin/bash

for i in {1000..1..-1}
do
	dir=$(cat direction.txt)
	unzip -o $i$dir".zip"
	clear
	rm $i"right.zip" $i"left.zip"
done
echo "DONE"
