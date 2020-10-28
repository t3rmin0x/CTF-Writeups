# Friends
> Points: 997

## Description
> The flag is created by putting it together

## Solution
App>>> <br>
![](friends.png)<br>
I set up a wireshark listener and started the app. It asks for data and shows the results in the app
```
POST /api/data HTTP/1.1
Content-Type: application/x-www-form-urlencoded
User-Agent: Dalvik/2.1.0 (Linux; U; Android 7.1.1; ONEPLUS A3010 Build/NMF26F)
Host: 37.152.186.157
Connection: Keep-Alive
Accept-Encoding: gzip
Content-Length: 0

HTTP/1.1 200 OK
Server: nginx/1.18.0 (Ubuntu)
Content-Type: application/json
Transfer-Encoding: chunked
Connection: keep-alive
Cache-Control: no-cache, private
Date: Wed, 28 Oct 2020 08:19:30 GMT
X-RateLimit-Limit: 60
X-RateLimit-Remaining: 59
Access-Control-Allow-Origin: *

[{"id":1,"name":"Bugs Bunny","avatar":"bugs_bunny.jpg","email":"gexeve3991@ngo1.com","address":"4617  Goodwin Avenue","gender":"male","age":"22","phone":"36213893021"},
{"id":2,"name":"Mickey Mouse","avatar":"mickey_mouse.jpg","email":"aufgetretenen@iatarget.com","address":"3844  Stiles Street","gender":"male","age":"28","phone":"12369532255"},
{"id":4,"name":"Bart Simpson","avatar":"bart_simpson.jpg","email":"buccinator@usabrains.us","address":"2418  Loving Acres Road","gender":"male","age":"35","phone":"55634559910"},
{"id":3,"name":"Popeye","avatar":"popeye.jpg","email":"hypnotoxin@lerepo.ga","address":"New Jersey popeye Street","gender":"male","age":"43","phone":"22361255893"},
{"id":5,"name":"Patrick Star","avatar":"patrick_star.jpg","email":"patrick_star@gmail.com","address":"Richmond 2136  Queens Lane","gender":"male","age":"18","phone":"41223365236"},
{"id":6,"name":"Homer Simpson","avatar":"homer_simpson.jpg","email":"vakantietij@walmartshops.com","address":"Timber Oak Drive","gender":"male","age":"47","phone":"99632531930"},
{"id":7,"name":"Olive Oyl","avatar":"olive_oyl.jpg","email":"senpakuh@vidred.tk","address":"Ocala Rhapsody Street","gender":"female","age":"52","phone":"89633366552"},
{"id":8,"name":"Sylvester","avatar":"sylvester.jpg","email":"emergera@didacvidal.com","address":"Tigard 2285  Kincheloe Road","gender":"male","age":"31","phone":"77632351752"}]
```
But the phone number isn't shown...<br>
![](details.png)<br>
Concatenating them gives the flag
## Flag
> RaziCTF{3621389302112369532255556345599102236125589341223365236996325319308963336655277632351752}
