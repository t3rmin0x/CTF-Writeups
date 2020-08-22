## Challenge: Shark On Wire

Opening the pcap file in Wireshark and searching for keyword "password" gives the flag
```
hey airisatou I want to inform you your password is pCTF{sh4rk_1n_th3_w1r3} just to remind you please change your password and don't
```
## Flag:
>pCTF{sh4rk_1n_th3_w1r3}

## Challenge: Key

Seaching for the keyword "key" brings you to a data where a public and a private key is written. Part of it:-
```
9YG7sjsId8rCoSjik+EHB3mKRjdYio7BQSs4UCvkHduG6L7RjALTVRM9Olc3h6q
iGadijzWhnNPNvB0k4Yd9Xuw56UmXdQKRGK2jwcx7e//U84I
=57Ft
-----END PGP PUBLIC KEY BLOCK-----
ââ[silver@parrot]â[~/Desktop/Phantomctf3/smtpsniffer]
ââââ¼ $cat priv.asc 
-----BEGIN PGP PRIVATE KEY BLOCK-----

lQdGBF89RWUBEACnR7BgBLMwSF7nyodEpFU17vB8sYxHj4FEVEJoELEcUoSz9Wxd
sEWMuHJBU45dSL1U88N/LLSCRdG67fk6PnftSufGnSwmLfEYnd6FnSFITwBwwk7c
```
So we take the PGP key into a file and run gpg2john on it. The hash gives the flag. End part:-
```
60*a83b4a1706809cc7:::argenestel (pCTF{N0t_A_g00d_Plac3}) <heyhello@heyhello.weeb>::priv.asc
```
## Flag:
>pCTF{N0t_A_g00d_Plac3}

## Challenge: Encrypted

In the stream we got a hex-data as:-
```
....ca25524508fb64c2aaa2cc231acb9353d9bb2ea128d7650170f7c0ed9fab
c4e055814a13209138d0
I am sending hex data so please look into it i encrypted it
using keys

```
Running john on the hash gives the password of the hash as "password"
Then we import the private key in gpg with the password "password"
```bash
gpg --import private.key
```
Then we store the above data in a file and decrypt with gpg
```bash
root@user:~/Documents/Phantom_CTF/Key# gpg -d download.dat 
gpg: encrypted with 4096-bit RSA key, ID 7F2BF2481707331E, created 2020-08-19
      "argenestel (pCTF{N0t_A_g00d_Plac3}) <heyhello@heyhello.weeb>"
hello here's your flag
pCTF{pGp_w0rks_wid_str0ng_p4ss}
regards sysadmin ;)
```
## Flag:
>pCTF{pGp_w0rks_wid_str0ng_p4ss}
