from scapy.all import *
from PIL import Image

pcap = rdpcap("mysquare.pcapng")

file = []
print("[+] Extracting Data")
for i in pcap[UDP]:
    query = (i[DNS].qd.qname.decode())
    if len(query) == 69:
        file.append(query.split('.')[0])

img = Image.new("1", (50,50), 255)
data = img.load()

print("[+] Creatng Imaage")
for i in range(50):
    for j in range(50):
        data[i,j] = 0 if file[i][j]=='0' else 255

img.save("QR.png")
