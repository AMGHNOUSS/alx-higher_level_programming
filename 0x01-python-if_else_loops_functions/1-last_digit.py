#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number % 10 == 0:
    print(f"Last digit of {number:d} is 0 and is 0")
elif number % 10 > 5:
    print(f"Last digit of {number:d} is {number % 10 : d} and is greater than 5")
else:
    print(f"Last digit of {number:d} is {number % 10: d} and is less than 6 and not 0")
