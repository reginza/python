import random


def del_not_uniq_elem(a_list, i):
    if a_list.count(i) > 1:
        while a_list.count(i) != 0:
            a_list.remove(i)
    return a_list


one_list = [random.randint(0, 10) for i in range(20)]
print(f'Исходный лист: {one_list}')

for i in one_list[0: -1]:
    one_list = del_not_uniq_elem(one_list, i)
print(f'Результат: {one_list}')
