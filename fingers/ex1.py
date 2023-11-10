"""
Finger exercise: Write a program that examines three variables—
x, y, and z—and prints the largest odd number among them. If none
of them are odd, it should print the smallest value of the three.
"""

x = 22
y = 42
z = 44
largest = 0

if x % 2 != 0:
    largest = x
if y % 2 != 0 and y > largest:
    largest = y
if z % 2 != 0 and z > largest:
    largest = z
if largest != 0:
    print(largest)
else:
    if x < y and x < z:
        print(x)
    elif y < x and y < z:
        print(y)
    else:
        print(z)
