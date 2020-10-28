# Recurzip
> Points: 955

## Description
> You download the file, you stay in this challenge, and I show you how deep the file goes. Remember: all I'm offering is the flag. Nothing more.

## Solution
> It's a Zip which contains recursively zipped file of 10,000 times
Written a bash script for that
```sh
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
```
It returns `flag.txt`

## Flag
> RaziCTF{wh3lp_th4t_w4s_e4sy_en0ugh}
