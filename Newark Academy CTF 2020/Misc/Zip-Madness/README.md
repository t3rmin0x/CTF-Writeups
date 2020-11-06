# Zip-Madness
> 175 points

## Description
> Evan is playing Among Us and just saw an imposter vent in front of him! Help him get to the emergency button by following the directions at each level. <br>
> [File](flag.zip)

## Solution
1000 zip files! ( x_x )

Everye zip file contains a file which tells us which zip to decompress next. A simple bash script will do the work.
### Script: [mad.sh](mad.sh)
```sh
#!/bin/bash

for i in {1000..1..-1}
do
        dir=$(cat direction.txt)
        unzip -o $i$dir".zip"
        clear
        rm $i"right.zip" $i"left.zip"
done
echo "DONE"

```
## Flag
> **nactf{1_h0pe_y0u_d1dnt_d0_th4t_by_h4nd_87ce45b0}**
