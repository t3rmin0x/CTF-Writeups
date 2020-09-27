## Challenge: Source
>Don't know source is helpful or not !!
http://web.darkarmy.xyz<br>
[File](https://mega.nz/file/K011ACaL#S6kfjaYxN_cOcYHYzBKpKKsqAf3dh7PS0-lKFIuGjZA)
## Solution
> We are given the source the source code of the php of the page.
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
