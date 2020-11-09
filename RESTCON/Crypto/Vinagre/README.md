# Vinagre
esolang, Vigenère cipher, 100 points

## Description
> There is this key and a Encoded Data given to you can you find the hidden flag?

> Flag Format : RESTCON{<- flag ->}

> Download Files :

> [File 1](Encoded.txt)

> [File 2](key-enc.txt)

## Solution

### Part I

I can't thank you enough [CyberChef](https://gchq.github.io/CyberChef). 
Just base32 decode and then hex decode the data from the **Encoded.txt**. The result was something like this...
```
++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>++++++++.--.+++++.---------.++++++++.++++++++++.--------------.>+++++++++++++++++++++++.<++++++.<++++++++++++++++++..>----------.+++++++++++++++++++++++.-----.<.+.>-------------------.++++.>++.
```

It's the Brainfuck esolang and decoding it [here](https://www.dcode.fr/brainfuck-language) results in `NLQHPZL{R00H_Z01GK}`.
Then I remembered that it can be a **Vigenère cipher** and also we are given the `key-enc.txt`.

### Part 2

The `key-enc.txt` file had something that looked like **Morse code** and decoding that gave us **Binary** data.
If we decode the **Binary** we'll get **Hex** and then **hex-decoding** gave us this...

```9 44 999 666 66 555 999 555 33 8 8 33 777 7777```

Pretty weird combo right?

After googling a lot, I found that it's `Multi-tap Phone Cipher (SMS)` which can be decoded [here](https://www.dcode.fr/multitap-abc-cipher). The result was...
```
WHYONLYLETTERS
```

This could be the key of our **Vigenère cipher**.

So I used [Dcode.fr](https://www.dcode.fr/vigenere-cipher) to decrypt the cipher with key `WHYONLYLETTERS` and got the flag.

> Flag: RESTCON{G00D_G01NG}
