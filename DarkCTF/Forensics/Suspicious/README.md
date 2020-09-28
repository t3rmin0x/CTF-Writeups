# Suspicious
> Points: 460

## Description
> Suspicious software created a key. I want that key to track that software.<br>
`File` Same as PowerShell

## Solution
Read the 1st part [link](https://github.com/t3rmin0x/CTF-Writeups/blob/master/DarkCTF/Forensics/Powershell/README.md)<br>
I opened the `Suspicious.reg` file in sublime text and searched for `suspicious`keyword and got this
```
[HKEY_USERS\S-1-5-21-1473425136-1446414652-728660776-1000\Software\Suspicious]
@="ZGFya0NURntIM3IzXzFzXzV1NXAxYzEwdXN9"
```
Decoded base64 and got flag.
## Flag
>darkCTF{H3r3_1s_5u5p1c10us}
