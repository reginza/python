import random
from functools import reduce


def my_func(prev_el, el):
    return prev_el + el


one_list = [random.randint(100, 1000) for i in range(20)]
print(one_list)

print(reduce(my_func, one_list))
