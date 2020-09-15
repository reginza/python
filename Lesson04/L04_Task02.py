import random
one_list = [random.randint(0, 100) for i in range(10)]
print(one_list)

two_list = []
a = 1000
for i in one_list:
    if i > a:
        two_list.append(i)
    a = i
print(two_list)
