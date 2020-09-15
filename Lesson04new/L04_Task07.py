from itertools import count
from math import factorial
from random import randint


def generator():
    for el in count(1):
        yield factorial(el)


n = generator()
a = randint(1, 10)
x = 0
for el in n:
    if x < a:
        print(el)
        x += 1
    else:
        break
