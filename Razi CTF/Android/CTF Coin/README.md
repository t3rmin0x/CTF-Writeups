# CTF Coin
> Points: 991

## Description
> Make your CTF Coins Unlimited (more than 1000000000000000)

## Solution
App >>><br>
![](ctf_coin.png)<br>
We can buy one coin at a time... but we have to make it that amount... So I intercepted the network data with Wireshark and saw some requests.<br>
![sniff.png]()<br>
So I changed the value of Coins JSON and send a request with Burp Suite Repeater<br>
![burp.png]()

## Flag
> RaziCTF{ZmRzdnNkRlNEcWUzQFFxZURXRUZEU1ZGU0RTNTVkc2Y1ZmV2c0RGcnEzNSRSI3J3ZnNlZnJ3IyQjJSNA}
