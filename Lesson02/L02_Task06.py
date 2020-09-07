my_list = []
my_list1 = []
dic = {}
step = 1
name = "Наименование"
price = "Цена"
quantity = "Количество"
unit = "Единица"
d = {name: [], price: [], quantity: [], unit: []}
product_quantity = int(input('Введите общее количество наименований товаров: '))
while product_quantity >= step :
    a = input("Наименование: ")
    b = input("Цена: ")
    c = input("Количество: ")
    n = input("Ед.измерения: ")
    dic = (step, {"название": a, "цена": b, "количество": c, "ед": n})
    d[name].append(a)
    d[price].append(b)
    d[quantity].append(c)
    d[unit].append(n)
    step = step + 1
    my_list.append(dic)
print(f'1. Часть задания: Структура данных "Товары": {my_list}')
print(f'2. Часть задания: Анализ данных": {d}')
