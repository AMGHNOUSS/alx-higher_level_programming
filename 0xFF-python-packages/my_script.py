
from my_math import abs, is_positive
from my_math.functions import add, mul, div, sub

a = 10
b = 5
c = -15
print(f"|{c}| = {abs.my_abs(c)}")

print(f"{a} + {b} = {add.my_add(a, b)}")
print(f"{a} - {b} = {sub.my_sub(a, b)}")
print(f"{a} * {b} = {mul.my_mul(a, b)}")
print(f"{a} / {b} = {div.my_div(a, b)}")

print(f"{c} is positive : {is_positive.my_is_positive(c)}")
print(f"{a} = {is_positive.my_is_positive(a)}")