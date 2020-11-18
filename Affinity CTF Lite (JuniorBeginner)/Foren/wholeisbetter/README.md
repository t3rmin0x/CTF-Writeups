# wholeisbetter
> Points 378

## Description
> :arrow_down: [There_is_a_flag_somewhere.pdf](There_is_a_flag_somewhere.pdf)

## Sol
```zsh
┌──(root 🌀 kali)-[~/Downloads/affinityCTF/foren]
└─# exiftool There_is_a_flag_somewhere.pdf                                                                                                                                                1 ⨯
ExifTool Version Number         : 12.09
File Name                       : There_is_a_flag_somewhere.pdf
Directory                       : .
File Size                       : 16 kB
File Modification Date/Time     : 2020:11:17 02:39:53-05:00
File Access Date/Time           : 2020:11:17 02:40:41-05:00
File Inode Change Date/Time     : 2020:11:17 02:40:22-05:00
File Permissions                : rw-r--r--
File Type                       : PDF
File Type Extension             : pdf
MIME Type                       : application/pdf
PDF Version                     : 1.7
Linearized                      : No
Page Count                      : 1
Language                        : pl-PL
Tagged PDF                      : Yes
XMP Toolkit                     : Image::ExifTool 10.80
Creator                         : Li4tLS0tLi4uLS0tLS0tLi4tLS0tLS0uLi4tLS0tLi4uLS0tLS0tLi4tLS0tLS0uLi4uLS0tLS4uLS0tLS0tLi4tLS4uLS0uLi4tLS0tLi4uLS0tLS0tLi4tLS0tLS0uLi0tLi4uLS0uLi0tLS0tLS4uLS0tLS0tLi4uLS0tLS4uLi0tLS0tLi4uLi0tLS0uLi4tLS0tLS0uLi4tLS0tLi4uLS0tLS4uLgo=#1
Subject                         : Li0tLS0tLS4uLS0tLS4uLi4tLS0tLi4uLi0tLi4uLi4uLi4tLS4uLi4tLS0tLi4uLi0tLS4uLi4uLi4tLS4uLi4tLS0tLS0uLi0tLS0tLS4uLi4tLS4uLi4tLS0tLi4uLi0tLi0uLS0uLi0tLS0uLi4uLi4tLS4uLi4tLS0tLS0uLi0tLi4tLS4uLS0tLS0tLi4uLi0tLi4uLi0tLS0tLS4uLi4uLS0tLgo=#3
Author                          : Li0tLi4tLS4uLS0uLi4uLi4tLS4uLi4uLi0tLi4tLS4uLi4tLS4uLi4tLS4uLi4uLi4uLS0uLi4uLi4tLS4uLi4tLS4uLS0uLi0tLi4tLS4uLi4tLS4uLi4tLS4uLi4uLi0tLi4uLS0uLi0tLi4uLi4uLi4tLS4uLi4tLS4uLS0uLi0tLi4tLS4uLS0uLi0tLi4uLi0tLi4uLi0tLi4tLS4uLi4tLS4uLgo=#4
Producer                        : Li0tLi4tLS4uLS0uLi4uLi4tLS4uLi4uLi4tLS0tLi4uLi4tLS4uLi4tLS4uLi4uLi4uLS0tLS4uLS0tLS0tLi4tLS4uLS0uLi0tLi4tLS4uLi4tLS4uLi4tLS0tLS0uLi0tLi4uLS0uLi0tLS0tLS4uLi4tLS4uLi4tLS4uLS0uLi0tLS0tLi4uLS0uLi0tLi4uLi0tLi4uLi0tLi4tLS4uLS0tLS4uLgo=#5
Keywords                        : Li0tLi4tLS4uLS0uLi4uLi4tLS4uLi4uLi0tLi4tLS4uLi4tLS4uLi4tLS4uLi4uLi4uLS0uLi4uLi4tLS4uLi4tLS4uLS0uLi0tLi4tLS4uLi4tLS4uLi4tLS4uLi4uLi0tLS4tLS0uLi0tLi4uLi4uLi4tLS4uLi4tLS4uLS0uLi0tLi4tLS4uLS0uLi0tLi4uLi0tLi4uLi0tLi4tLS4uLi4tLS4uLgo=#2
                                                                            
```
Base64 decoded the last 4 lines in CyberChef then:

![solve.gif](solve.gif)

## Flag
> **AFFCTF{IHATEMETADATA}**
