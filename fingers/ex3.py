"""
Finger exercise: Replace the comment in the following code with a
while loop.
"""

num_x = int(input('How many times should I print the letter X? '))
to_print = ''

while len(to_print) < num_x:
    to_print += 'X'

print(to_print)
