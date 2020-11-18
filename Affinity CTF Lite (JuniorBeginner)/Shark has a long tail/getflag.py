#!/usr/bin/env python3
import os

os.system("tshark -r SharkHasALongTail.pcap -T fields -e tcp.len > out.txt")
print("tshark is closed!\nFinal output:\n")
out = open("./out.txt").read().strip().split('\n')
print(''.join(chr(int(c)) for c in out))

