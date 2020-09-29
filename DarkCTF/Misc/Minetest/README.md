# Minetest 1
> Points: 303

## Description
>Just a sanity check to see whether you installed Minetest successfully and got into the game.<br>
[File](https://mega.nz/file/zxlhlAYL#1SbgYkhBMHqyeCWNNHNIASAxanpEMLi2CGxHjRod4k8)

## Solution
This was the best challenge for me in the whole event bcz I love games :) #gamer<br>
We are given `mods` and `worlds` folder of Minetest game. I downloaded the game on [windows](https://www.minetest.net/downloads/)
Copied the folders in the game directory and started the game. 
<p align="center"><img src = "game.png" height="300" width="550"></p><br>

I was greeted with this.

<p align="center"><img src = "Screenshot_1.png" height="300" width="587"></p>

Roaming around I see: There are 16 switches from which connections come and form a logical circuit with and, or , not gates
This means I have to on/off (0 or 1) the switches and solve the series of gates.

![](image.png)

Completing a part of the connection brightens the circuit.
Finally completing the circuit triggers something (code block perhaps) and gives us the 1st flag and instructions to the next one.<br>
<p align="center"><img src="trigger.gif"></p>

## Flag
>DarkCTF{y0u_5ucess_fu11y_1ns7alled_m1n37e57}
