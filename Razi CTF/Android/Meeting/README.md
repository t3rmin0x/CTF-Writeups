# Meeting ![badge](https://img.shields.io/badge/Post%20CTF-Writeup-success)
> Points: 1000

## Description
> Mickey Mouse goes to visit his friend and orders two pizzas in a phone call. Deliver the pizza to him. Hint: Related to Steganography

## Solution
Read first part [here](https://github.com/t3rmin0x/CTF-Writeups/tree/master/Razi%20CTF/Android/Friends)<br>
As the hint states steganography it's something related to images... So I re-installed the app and monitored traffic with wireshark. I saw the images are downloaded and not inside the apk itself.
![](sniff.png)<br>
I extracted the image from wireshark. Made a wordlist of the phone numbers we got. Ran stegcracker.

## Flag
> RaziCTF{}
