"""
Finger exercise: Write a program that asks the user to input 10
integers, and then prints the largest odd number that was entered. If
no odd number was entered, it should print a message to that effect.
"""

count = 10
loop = 0
answer = 0
num = 0
while loop < count:
    num = int(input("Enter an integer: "))
    loop += 1
    if num % 2 != 0 and num > answer:
        answer = num
    
if answer == 0:
    print("No odd number was entered")
else:
    print(answer)
