#!/bin/sh

filename=$(ls | grep zip | cut -d'.' -f 1)

while [ ${#filename} != 0 ]
do
	filename=$(ls | grep zip | cut -d'.' -f 1)
	password=$(echo $filename | base64 -d)
	filename="${filename}.zip"

	unzip -P $password $filename
	rm $filename
	clear
done
