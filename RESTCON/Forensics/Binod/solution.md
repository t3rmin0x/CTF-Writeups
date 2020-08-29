# Binod
wireshark, pdf-analysis, 300 points

## Description
> Hey there, we recently came to know that a malware has spread across our network ever since Binod helped one of our Desk support team by giving an employee some malicious file.Your task is to check out this program and find out the flag , remember don't believe what you see.

> [Challange File](logs.pcapng)

> FLAG Format : RESETCON{<- Flag ->}

## Solution
Analyzing the logs.pcapng file in Wireshark, I got the [binod.exe](binod.exe) file. Actually it is a PDF file with base64 encoded strings. Luckily we have 
[Cyberchef](https://gchq.github.io/CyberChef/) and decoding the base64 string gives us repeated "Binod Binod...." strings. :(

Then I tried to use `strings` on binod.exe (`pdf-parser` showed a better result actually) and got the [list of objects](https://medium.com/@tho.le/pdf-forensics-introduction-part-1-6e8232935828) from the PDF.

This string object caught my eye...

```bash
3 0 obj
/Type /Action
/S /JavaScript
/JS <616C65727428227265736574636F6E7B62316E30645F31245F6330306C5F31246E375F68333F7D22293B0A>
endobj
```
Hex decoding it gives us the flag.

```python
>>> bytes.fromhex('616C65727428227265736574636F6E7B62316E30645F31245F6330306C5F31246E375F68333F7D22293B0A')
b'alert("resetcon{b1n0d_1$_c00l_1$n7_h3?}");\n'
>>>
```
> Flag : resetcon{b1n0d_1$_c00l_1$n7_h3?}
