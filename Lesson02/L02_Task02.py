old_list = [int(i) for i in input("Введите числа через пробел: ").split()]
new_list = []

for i in range(0, len(old_list) -1, 2):
    x, y = old_list[i], old_list[i + 1]
    new_list.append(y)
    new_list.append(x)
if len(old_list) % 2 != 0:
    new_list.append(old_list[len(old_list) - 1])
print(new_list)
