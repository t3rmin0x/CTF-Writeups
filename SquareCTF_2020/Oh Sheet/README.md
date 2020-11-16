# Oh Sheet
> Points: 200 <br>
> Solved by r3yc0n1c

## Description
> Someone very cheeky decided to encrypt their secret message in Google Sheets. What could they be hiding in plain sight? <br>
> Curious! Click on the link below to find out more: <br>
> [https://docs.google.com/spreadsheets/d/15PFb_fd6xKVIJCF0b0XiiNeilFb-L4jm2uErip1woOM/edit#gid=0](https://docs.google.com/spreadsheets/d/15PFb_fd6xKVIJCF0b0XiiNeilFb-L4jm2uErip1woOM/edit#gid=0)

## Solution
* Make a copy of the Sheet - [Copy of Oh Sheet!](https://docs.google.com/spreadsheets/d/1aYVG9C1-bqtysSSLKuJRA3WoekFO-fTpDww_Lt8VeII/edit?usp=sharing)
* Clear the formatting [ Format > Clear Formatting ] because they hid some texts by changing the text color to white.
* Script - [apex.py](apex.py)
* I used [pypy3](https://www.pypy.org/) for the first time on windows 10 machine to do this brute-force [[it's relatively faster](https://stackoverflow.com/questions/59050724/whats-the-differences-python3-and-pypy3#:~:text=On%20a%20suite%20of%20benchmarks,in%20beta%2C%20targets%20Python%203.)]
* Guess the key

## Flag
> **flag{squarectf}**
