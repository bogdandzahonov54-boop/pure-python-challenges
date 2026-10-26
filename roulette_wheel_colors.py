"""
Task Description:
Roulette Wheel Colors

On a roulette wheel, the pockets are numbered from 0 to 36. 
The colors of the pockets are as follows:
- Pocket 0 is green.
- For pockets 1 to 10: odd-numbered pockets are red, even-numbered are black.
- For pockets 11 to 18: odd-numbered pockets are black, even-numbered are red.
- For pockets 19 to 28: odd-numbered pockets are red, even-numbered are black.
- For pockets 29 to 36: odd-numbered pockets are black, even-numbered are red.

Write a program that reads the pocket number and displays whether the pocket is green, red, or black. 
The program must display an error message if the user enters a number outside the 0 to 36 range.
"""

# Read input integer representing the roulette pocket number
a = int(input())

# Condition 1: Check for the special green pocket
if a == 0:
    print("зеленый")

# Condition 2: Range 1 to 10 (Even -> Black, Odd -> Red)
elif 1 <= a <= 10:
    if a % 2 == 0:
        print("черный")
    else:
        print("красный")

# Condition 3: Range 11 to 18 (Even -> Red, Odd -> Black)
elif 11 <= a <= 18:
    if a % 2 == 0:
        print("красный")
    else:
        print("черный")

# Condition 4: Range 19 to 28 (Even -> Black, Odd -> Red)
elif 19 <= a <= 28:
    if a % 2 == 0:
        print("черный")
    else:
        print("красный")

# Condition 5: Range 29 to 36 (Even -> Red, Odd -> Black)
elif 29 <= a <= 36:
    if a % 2 == 0:
        print("красный")
    else:
        print("черный")

# Fallback block: Handle out-of-bounds input values
else:
    print("ошибка ввода")
