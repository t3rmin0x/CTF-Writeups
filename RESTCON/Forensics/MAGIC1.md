# MAGIC : 1
QR, hash-cracking, 20 points

## Description
[File](output.png)

NOTE: FLAG IS IN PLAIN TEXT

## Solution

Decoding the QR with `zbarimg` gives us `RESTCON{29a9df89e2858e5a25c83b6a00352d19}` (we can also use online site like [ZXing](https://zxing.org/w/decode.jspx))

Then we can crack the md5 using [crackstation](https://crackstation.net/) and get the flag.

> Flag: RESTCON{mirr0r}
