from itertools import count, cycle


for el in count(10):
    if el > 20:
        break
    else:
        print(el)


c = 0
for el in cycle("Hello"):
    if c > 4:
        break
    print(el)
    c += 1
