# Wolfie's Contact
> Points: 221

## Description
>Wolfie is doing some illegal work with his friends find his contacts.<br>
[File](https://mega.nz/file/rs9XCCyK#MuQcqPYUJ1mQtJZhRQInuwvBS7wazVm2DyMgp-edAgg)

## Solution
For initial recon I mounted it with `ewftools` in my Kali VM instead of Autopsy (will use later). The files are...
```bash
⚡ root@ignite ~/Documents/darkCTF/mountpoint> ls -la
total 3248
drwxrwxrwx 1 root root    8192 Sep 25 06:19  .
drwxr-xr-x 6 root root    4096 Sep 28 12:36  ..
-rwxrwxrwx 1 root root    2560 Sep 20 13:59 '$AttrDef'
-rwxrwxrwx 1 root root       0 Sep 20 13:59 '$BadClus'
-rwxrwxrwx 1 root root    9600 Sep 20 13:59 '$Bitmap'
-rwxrwxrwx 1 root root    8192 Sep 20 13:59 '$Boot'
drwxrwxrwx 1 root root       0 Sep 20 13:59 '$Extend'
-rwxrwxrwx 1 root root 3145728 Sep 20 13:59 '$LogFile'
-rwxrwxrwx 1 root root    4096 Sep 20 13:59 '$MFTMirr'
drwxrwxrwx 1 root root       0 Sep 20 14:00 '$RECYCLE.BIN'
---------- 1 root root       0 Sep 20 13:59 '$Secure'
-rwxrwxrwx 1 root root  131072 Sep 20 13:59 '$UpCase'
-rwxrwxrwx 1 root root       0 Sep 20 13:59 '$Volume'
drwxrwxrwx 1 root root    4096 Sep 20 14:22  contacts
drwxrwxrwx 1 root root       0 Sep 20 14:26  deals
drwxrwxrwx 1 root root       0 Sep 20 14:28  documents
drwxrwxrwx 1 root root    4096 Sep 25 06:23  downlaods
drwxrwxrwx 1 root root       0 Sep 21 00:25  images
drwxrwxrwx 1 root root       0 Sep 20 15:00  moives
drwxrwxrwx 1 root root       0 Sep 20 14:58  money
drwxrwxrwx 1 root root       0 Sep 20 14:55  music
drwxrwxrwx 1 root root       0 Sep 21 00:25 'not important files'
drwxrwxrwx 1 root root       0 Sep 20 14:10  NT
drwxrwxrwx 1 root root       0 Sep 20 14:10  PerfLogs
drwxrwxrwx 1 root root       0 Sep 20 14:10  pics
drwxrwxrwx 1 root root       0 Sep 20 14:10 'Progaram Files'
drwxrwxrwx 1 root root       0 Sep 25 06:09 'Program Files'
drwxrwxrwx 1 root root       0 Sep 25 06:09  socials
drwxrwxrwx 1 root root       0 Sep 20 23:43 'System Volume Information'
drwxrwxrwx 1 root root       0 Sep 25 06:11  targets
drwxrwxrwx 1 root root       0 Sep 20 14:10  tools
drwxrwxrwx 1 root root       0 Sep 20 14:10  users
drwxrwxrwx 1 root root       0 Sep 20 14:10  work
```
I got into the `contacts` folder and there are some XML files.
```bash
⚡ root@ignite  ~/Documents/darkCTF/mountpoint/contacts  ls   
 agent.contact  'Agent P.contact'   broker.contact   dealer.contact   Ferb.contact  'Money Giver.contact'   Phineas.contact   target.contact   wolfie.contact
```
There are parts of the flag in the notes section of the XML files.
```bash
⚡ root@ignite  ~/Documents/darkCTF/mountpoint/contacts  cat * | grep Notes
        <c:Notes c:Version="1" c:ModificationDate="2020-09-20T18:19:52Z">C0ntacts_
</c:Notes><c:CreationDate>2020-09-20T18:19:12Z</c:CreationDate><c:Extended xsi:nil="true"/>
        <c:Notes>darkCTF{</c:Notes><c:CreationDate>2020-09-20T18:18:41Z</c:CreationDate><c:Extended xsi:nil="true"/>
        <c:Notes>1mp0rtant}</c:Notes><c:CreationDate>2020-09-20T18:21:20Z</c:CreationDate><c:Extended xsi:nil="true"/>
        <c:Notes>4re_
</c:Notes><c:CreationDate>2020-09-20T18:19:55Z</c:CreationDate><c:Extended xsi:nil="true"/>
        <c:Notes>All HAil Wolfiee!!!</c:Notes><c:CreationDate>2020-09-20T18:17:25Z</c:CreationDate><c:Extended xsi:nil="true"/>
```
Adding all them we get the flag.
## Flag
>darkCTF{C0ntacts_4re_1mp0rtant}
