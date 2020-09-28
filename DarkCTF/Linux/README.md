# Challenge: Linux Starter
>Don't Try to break this jail<br>
ssh wolfie@linuxstarter.darkarmy.xyz -p 8001 password : wolfie

## Solution
We get into a `rbash` shell. We run some simple commands and get the flag<br>
```bash
wolfie:~$ cat *
cat: bin: Is a directory
cat: imp: Is a directory
wolfie:~$ cat imp/*
darkCTF{h0pe_y0u_used_intended_w4y}
```
## Flag:
>darkCTF{h0pe_y0u_used_intended_w4y}

# Challenge: Find-me
>Mr.Wolf was doing some work and he accidentally deleted the important file can you help him and read the file?<br>
ssh ctf@findme.darkarmy.xyz -p 10000 password: wolfie

## Solution
As the question suggests about the delete file. I went to `/proc/10/fd` and found 3 files there.
```bash
```
I found out there are 2 users in the home directory.
```bash
```
So I used the above password to gain access to `wolf2`. And searched for files in it.
```bash
```
## Flag:
>

# Challenge: Secret Vault
>There's a vault hidden find it and retrieve the information. Note: Do not use any automated tools.<br>
ssh ctf@vault.darkarmy.xyz -p 10000

## Solution
I found the vault file
```bash
dark@941b05d2d95a:/home/dark$ find /home -type f
/home/.secretdoor/vault
/home/dark/.bash_logout
/home/dark/.profile
/home/dark/.bashrc
dark@941b05d2d95a:/home/dark$ cd /home/.secretdoor/
dark@941b05d2d95a:/home/.secretdoor$ ls
vault
dark@941b05d2d95a:/home/.secretdoor$ ./vault 1234

wrong pin: 1234
```
Wrote a script to bruteforce PIN
```bash
dark@5a95bae226e7:/home/.secretdoor$ nr=0; while true; do nr=$((nr+1)); if [[ $(./vault $nr) != *"wrong"* ]]; then ./vault $nr; echo $nr; fi; done;

Vault Unlocked :A79Lo6W?O%;D;Qh1NIbJ0lp]#F^no;F)tr9Ci!p(+X)7@ 
8794
```
Base85 decode the string gives the flag.

## Flag:
>darkCTF{R0bb3ry_1s_Succ3ssfullll!!}

# Challenge: Squids
>Squids in the linux pool<br>
ssh ctf@squid.darkarmy.xyz -p 10000 password: wolfie

## Solution
I found a interesting SUID binary.
```bash
```
It can run `cat` command as root

## Flag:
>
