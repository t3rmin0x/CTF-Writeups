# Goblet of Fire
> 953 points ( 1st :drop_of_blood: )

# Description
> I think Granger is smart enough to help you solve this challenge! <br>
> [File](Goblet_of_Fire.txt)

# Solution
We can observe that the given text file contains weird amount of tabs and spaces in weird positions.
Little bit of googling tells us about [stegsnow - whitespace steganography](http://manpages.ubuntu.com/manpages/bionic/man1/stegsnow.1.html).

I tried to extract the hidden message but it only gives us garbage values :(
```sh
root@kali:~/Downloads/razi/steg/Goblet of Fire# stegsnow Goblet\ of\ Fire.txt
�ka�����F�Å1�CN�y���K�Qa�
```
From the docs, I found that it has a **password mode** too. Now, the challenge was to find the password. I tried some random passwords but nothing worked so far.

Then I thought the Description may give us a hint. I tried **Granger** as password and it worked!
```sh
root@kali:~/Downloads/razi/steg/Goblet of Fire# stegsnow -p "Granger" Goblet\ of\ Fire.txt
RaziCTF{175_ju57_tabs_4nd_5p4c35}
```

## Flag
> **RaziCTF{175_ju57_tabs_4nd_5p4c35}**
