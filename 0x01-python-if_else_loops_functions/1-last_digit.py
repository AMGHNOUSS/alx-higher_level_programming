#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
x = number
y = number
if number < 0:
    x = -number
x = x % 10
if number > 0:
    if x == 0:
        print(f"Last digit of {y:d} is 0 and is 0")
    elif x > 5:
        print(f"Last digit of {y:d} is {x:d} and is greater than 5")
    else:
        print(f"Last digit of {y:d} is {x:d} and is less than 6 and not 0")
else:
    if x == 0:
        print(f"Last digit of {y:d} is 0 and is 0")
    else:
        print(f"Last digit of {y:d} is {-x:d} and is less than 6 and not 0")
