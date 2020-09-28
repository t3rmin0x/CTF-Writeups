# Duplicacy Within
> Points: 462

## Description
> Looks like Mr. Jones has found a secret key. Can you retrieve it like him?
>
> Format : darkCTF{hex value of key} <br>
>
> [check this](https://bit.ly/2Gjz2lL)
>
> `z1 = 0xc0e2d0a89a348de88fda08211c70d1d7e52ccef2eb9459911bf977d587784c6e`
>
> `z2 = 0x17b0f41c8c337ac1e18c98759e83a8cccbc368dd9d89e5f03cb633c265fd0ddc`

## Solution
Never did a challenge like this before so I googled the values and came up with this - 
[How I Hacked a Bitcoin Wallet: A Step By Step Guide...](https://35.244.241.141/hacking-a-bitcoin-wallet-642u36sa)

So, it is something related to **Bitcoin transaction vulnerability**. Luckily I found a script to exploit this.

Here is the [Original Script](https://ideone.com/wIV3dB).

I just made some changes and here it is...

```py
# https://www.blockchain.com/btc/tx/83415dded4757181c6e1c55104e2742a6f8cff05a9a46fbf029ae47b0054d511

import hashlib

p  = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
#r  = 0xd47ce4c025c35ec440bc81d99834a624875161a26bf56ef7fdc0f5d52f843ad1
#s1 = 0x44e1ff2dfd8102cf7a47c21d5c9fd5701610d04953c6836596b4fe9dd2f53e3e
#s2 = 0x9a5f1c75e461d7ceb1cf3cab9013eb2dc85b6d0da8c3c6e27e3a5a5b3faa5bab
z1 = 0xc0e2d0a89a348de88fda08211c70d1d7e52ccef2eb9459911bf977d587784c6e 
z2 = 0x17b0f41c8c337ac1e18c98759e83a8cccbc368dd9d89e5f03cb633c265fd0ddc

# r1 and s1 are contained in this ECDSA signature encoded in DER (openssl default).
der_sig1 = "30440220d47ce4c025c35ec440bc81d99834a624875161a26bf56ef7fdc0f5d52f843ad102202f88bf73d0f94a1e917d1a6e65ba15a9dbf52d0999c91f2c2c6bb710e018f7e001"

# the same thing with the above line.
der_sig2 = "30440220d47ce4c025c35ec440bc81d99834a624875161a26bf56ef7fdc0f5d52f843ad102203602aff824a32c19825425704546145d5fbc282ee912089923e824f46867647b01"

...

def show_results(privkeys):
	print "Posible Candidates..."
	for privkey in privkeys:
		hexprivkey = inttohexstr(privkey)
		# print "intPrivkey = %d"  % privkey
		# print "hexPrivkey = %s" % hexprivkey
		print "darkCTF{"+ hexprivkey +"}"
		# print "bitcoin Privkey (WIF) = %s" % base58_check_encode(hexprivkey.decode('hex'),version=128)

...


if __name__ == "__main__":
    main()
```
### Full Script - [btc_exploit.py](btc_exploit.py) 

### Output
```bash
┌──(root 🔱 r3yc0n1c)-[~/Downloads/darkCTF-finals/crypto]
└─# python btc_exploit.py                                                                                                                                                                   
sig1: 30440220d47ce4c025c35ec440bc81d99834a624875161a26bf56ef7fdc0f5d52f843ad102202f88bf73d0f94a1e917d1a6e65ba15a9dbf52d0999c91f2c2c6bb710e018f7e001
p: fffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141
sig2: 30440220d47ce4c025c35ec440bc81d99834a624875161a26bf56ef7fdc0f5d52f843ad102203602aff824a32c19825425704546145d5fbc282ee912089923e824f46867647b01
z1: c0e2d0a89a348de88fda08211c70d1d7e52ccef2eb9459911bf977d587784c6e
z2: 17b0f41c8c337ac1e18c98759e83a8cccbc368dd9d89e5f03cb633c265fd0ddc
Posible Candidates...
darkCTF{791198f7b09c5e63fc5798df41c4090d2265d8066e4d4a917a9d604f17ccf856}
darkCTF{12cba205306996b4fc6d9f6a4b920cebecf0c7b88b2b773af0c3b6a551b16339}
darkCTF{ed345dfacf96694b03926095b46df312cdbe152e241d2900cf0ea7e77e84de08}
darkCTF{86ee67084f63a19c03a86720be3bf6f1984904e040fb55aa4534fe3db86948eb}
                                                                           
```

## Flag
> darkCTF{791198f7b09c5e63fc5798df41c4090d2265d8066e4d4a917a9d604f17ccf856}


### Have some fun!
* Read - [Bitcoin transaction nonce reuse vulnerability](https://strm.sh/post/bitcoin-transaction-nonce-reuse/)
* Try the approach written in the Blog - [How I Hacked a Bitcoin Wallet: A Step By Step Guide...](https://35.244.241.141/hacking-a-bitcoin-wallet-642u36sa) 
using **[Sage Cell Server](https://sagecell.sagemath.org/)**

```sage
p  = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
r  = 0xd47ce4c025c35ec440bc81d99834a624875161a26bf56ef7fdc0f5d52f843ad1
s1 = 0x2f88bf73d0f94a1e917d1a6e65ba15a9dbf52d0999c91f2c2c6bb710e018f7e0
s2 = 0x3602aff824a32c19825425704546145d5fbc282ee912089923e824f46867647b
z1 = 0xc0e2d0a89a348de88fda08211c70d1d7e52ccef2eb9459911bf977d587784c6e
z2 = 0x17b0f41c8c337ac1e18c98759e83a8cccbc368dd9d89e5f03cb633c265fd0ddc

K = GF(p)

K((z1*s2 - z2*s1)/(r*(s1-s2)))
```
> Output : `54760946821827294169877095010530734624480634006478775701184416665424957864022`

> Decimal to Hex using [RapidTables](https://www.rapidtables.com/convert/number/decimal-to-hex.html))

> Output : `791198F7B09C5E63FC5798DF41C4090D2265D8066E4D4A917A9D604F17CCF856`
