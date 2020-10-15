# Just Listen
> 200 points

## Description
> Did you heard what he said ? <br>
> Flag format: flag{string} <br>
> :arrow_down: [file.txt](file.txt)

## Solution
* The `.txt` file has some unknow hex values which starts with `52 49 46 46`.
* A quick google search tells us they are the part of the header (magic bytes) of **WAV** Files. ([WAV File Signatures - File Signature Database](https://www.filesignatures.net/index.php?page=search&search=WAV&mode=EXT))
* Then I open the file in [CyberChef](https://gchq.github.io/CyberChef/) and saved it as [download.wav](download.wav).
* The audio file gives us a **pastebin.com** link where the flag is located.
* After trying some possibilities, I found the real url.
> URL: [https://pastebin.com/TJE2UNC6](https://pastebin.com/TJE2UNC6)
* Decoding the Base64 string gives us the flag!
```rb
root@kali:~/Downloads/stega/just_listen# echo "ZmxhZ3tZT1VfRElEX0xJU1RFTn0=" | base64 -d
flag{YOU_DID_LISTEN}
```

## Flag
> flag{YOU_DID_LISTEN}
