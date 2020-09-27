## Challenge: Flag of Life
>Help our adventurer in attaining the Flag of Life by defeating the Demon Guard Flageon.<br>
nc flagoflife.darkarmy.xyz 7001

## Solution
> Connecting with nc we get:
```bash
⚡ root@ignite  ~ nc flagoflife.darkarmy.xyz 7001
'Demon Guard Flageon: Who dares to disturb my slumber?
...
A human?
what is your name human?

You: ignite

Demon Guard Flageon: Listen close, ignite.
        To pass through you must give me a key of certain shape and size.
        I do not expect mere mortals to pass this test and win the Flag of Life.
        So here is a hint: the shape of the key is a square.
        But I will not tell you the size.
        You have 3 tries!


        | How lucky! Look in your backpack. You have a square-key-making device.
        | huh... weird thing to carry around if you ask me.
        | Anyways.
        | The problem is the device needs the edge length as input to make the key...

Input edge length: 1111111111111111111111

        | Device only takes positive integers as input |

Input edge length: 11

*mechanical whirring*
...
*pop*

Demon Guard Flageon: The size of your key is off by 121 sq cm.
        You have 1 more attempts left

Input edge length: 1

*mechanical whirring*
...
*pop*

Demon Guard Flageon: The size of your key is off by 1 sq cm.
        You have 0 more attempts left
```
Deductions:
We see its a C program, it only takes positive integer and square it and checks the difference of the value from the required value which is 0. So we need to overflow the squared value so it becomes 0.
` UINT_MAX + 1 = 0 ` which is 4294967295 + 1 = 4294967296. Square root of it is `65536`
```bash
Input edge length: 65536

*mechanical whirring*
...
*pop*

Demon Guard Flageon: Congratulation! You have completed this task.
        The Flag of Life is now your's

                ===============================================
                | darkCTF{-2147483648_c0m3s_aft3r_2147483647} |
                ===============================================

```
## Flag:
>darkCTF{-2147483648_c0m3s_aft3r_2147483647}
