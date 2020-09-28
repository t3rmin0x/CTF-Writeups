# Minesweeper
> Points: 463

## Description
> I'm lucky to be surrounded by even-minded people from all around. Flag is not in the regular format.<br>
Submit flag in darkCTF{flag} format.
[File](https://mega.nz/file/i0tATZqD#f3yeR8wVObm84UMjHL-aDCeVwLJoFUNbC60TJYtg_mU)

## Solution
We are given a file. The file states...
```
I'am lucky to be surrounded by even-minded people from all directions.
Flag is not in the regular format.
array = [[93, 91, 95, 88, 42, 78, 93, 91, 93, 93, 83, 73, 75, 67, 79, 93, 79, 75, 97, 85, 83, 85, 79, 87, 93, 83, 69, 87, 77, 89, 79, 81, 67, 69, 75, 95, 89, 89, 93, 95], 
[75, 85, 75, 96, 69, 70, 85, 95, 81, 97, 95, 75, 75, 85, 79, 77, 87, 69, 95, 77, 81, 81, 89, 79, 73, 93, 73, 93, 91, 97, 85, 85, 67, 87, 67, 89, 85, 95, 75, 71],
[83, 89, 73, 80, 76, 72, 79, 73, 71, 71, 79, 91, 91, 69, 83, 89, 73, 67, 67, 85, 69, 85, 81, 89, 93, 75, 97, 77, 75, 83, 85, 79, 73, 75, 73, 79, 75, 83, 83, 69],
...
```
It is a 52x40 2D array which resembles blocks of the cult classic game `Minesweeper`.
As the question states about being surrounded by even-minded... It means we have to find those values which are surrounded by even numbers on all 8 sides. Wrote a scipt to do that.
```py
array = (
	(93, 91, 95, 88, 42, 78, 93, 91, 93, 93, 83, 73, 75, 67, 79, 93, 79, 75, 97, 85, 83, 85, 79, 87, 93, 83, 69, 87, 77, 89, 79, 81, 67, 69, 75, 95, 89, 89, 93, 95), 
	(75, 85, 75, 96, 69, 70, 85, 95, 81, 97, 95, 75, 75, 85, 79, 77, 87, 69, 95, 77, 81, 81, 89, 79, 73, 93, 73, 93, 91, 97, 85, 85, 67, 87, 67, 89, 85, 95, 75, 71), 
  ...
	(93, 69, 87, 103, 99, 127, 65, 107, 93, 113, 97, 81, 125, 127, 103, 97, 71, 125, 111, 127, 101, 73, 127, 93, 83, 105, 97, 119, 113, 109, 73, 81, 101, 83, 73, 87, 71, 93, 73, 67)
)

def is_even(n):
	if (n%2==0):
		return True
	else:
		return False

output = ""

for i in range(1,50):
	for j in range(1,39):
		left = 	array[i][j-1]
		right = array[i][j+1]
		up = 	array[i-1][j]
		down = 	array[i+1][j]
		d1 = 	array[i-1][j+1]
		d2 = 	array[i-1][j-1]
		d3 = 	array[i+1][j+1]
		d4 = 	array[i+1][j+1]
		if is_even(left) and is_even(right) and is_even(up) and is_even(down) and is_even(d1) and is_even(d2) and is_even(d3) and is_even(d3):
			output += chr(array[i][j])

print(output[::-1])
```
```bash
⚡ root@ignite ~/Documents/darkCTF> python3 solvemine.py 
FLaGISYOUHaVEOBSERVaTIONaNDPaTIENCE
```
## Flag
>darkCTF{YOUHaVEOBSERVaTIONaNDPaTIENCE}
