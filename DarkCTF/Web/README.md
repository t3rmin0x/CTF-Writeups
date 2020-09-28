# Challenge: Source
> Points: 101

## Description
>Don't know source is helpful or not !!
http://web.darkarmy.xyz<br>
[File](https://mega.nz/file/K011ACaL#S6kfjaYxN_cOcYHYzBKpKKsqAf3dh7PS0-lKFIuGjZA)

## Solution
We are given the source the source code of the php of the page.
```php
$web = $_SERVER['HTTP_USER_AGENT'];
if (is_numeric($web)){
      if (strlen($web) < 4){
          if ($web > 10000){
                 echo ('<div class="w3-panel w3-green"><h3>Correct</h3>
  <p>darkCTF{}</p></div>');
```
It takes the value from the User Agent and do some checks on it. The length of the value should be less than 4 and the value should be greater than thousand. PHP `is_numeric` function accepts exponential values. We change User Agent to `9e9` and go to the site and we get the flag.

## Flag:
>darkCTF{changeing_http_user_agent_is_easy}

# Challenge: Apache Logs
> Points: 113

## Description
>Our servers were compromised!! Can you figure out which technique they used by looking at Apache access logs.<br>
flag format: DarkCTF{}<br>
[File](https://mega.nz/file/m98S1YTC#WzatL7aoufzZZFO22u3595BruxD0VRsHx44WZgrpeho)

## Solution
We are given a apache log file. We see they are evidence of SQLI and some `fromCharCode` stuff.
```
192.168.32.1 - - [29/Sep/2015:03:37:34 -0400] "GET /mutillidae/index.php?page=user-info.php&username=%27+union+all+select+1%2CString.fromCharCode%28102%2C+108%2C+97%2C+103%2C+32%2C+105%2C+115%2C+32%2C+83%2C+81%2C+76%2C+95%2C+73%2C+110%2C+106%2C+101%2C+99%2C+116%2C+105%2C+111%2C+110%29%2C3+--%2B&password=&user-info-php-submit-button=View+Account+Details HTTP/1.1" 200 9582 "http://192.168.32.134/mutillidae/index.php?page=user-info.php&username=something&password=&user-info-php-submit-button=View+Account+Details" "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"
token=&username=CHAR%28121%2C+111%2C+117%2C+32%2C+97%2C+114%2C+101%2C+32%2C+111%2C+110%2C+32%2C+116%2C+104%2C+101%2C+32%2C+114%2C+105%2C+103%2C+104%2C+116%2C+32%2C+116%2C+114%2C+97%2C+99%2C+107%29&password=&confirm_password=&my_signature=&register-php-submit-button=Create+Account HTTP/1.1" 200 8015 "http://192.168.32.134/mutillidae/index.php?page=register.php" "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"
192.168.32.1 - - [29/Sep/2015:03:39:46 -0400] "GET /mutillidae/index.php?page=client-side-control-challenge.php HTTP/1.1" 200 9197 "http://192.168.32.134/mutillidae/index.php?page=user-info.php&username=%27+union+all+select+1%2CString.fromCharCode%28102%2C%2B108%2C%2B97%2C%2B103%2C%2B32%2C%2B105%2C%2B115%2C%2B32%2C%2B68%2C%2B97%2C%2B114%2C%2B107%2C%2B67%2C%2B84%2C%2B70%2C%2B123%2C%2B53%2C%2B113%2C%2B108%2C%2B95%2C%2B49%2C%2B110%2C%2B106%2C%2B51%2C%2B99%2C%2B116%2C%2B49%2C%2B48%2C%2B110%2C%2B125%29%2C3+--%2B&password=&user-info-php-submit-button=View+Account+Details" "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"
```
URL Decoded them, and then Decoded Ascii to get the flag

## Flag:
>DarkCTF{5ql_1nj3ct10n}
