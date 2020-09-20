# Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
import json

with open('data7.txt', 'r') as f:
    profit = {}
    average_profit = {}
    list_full = []
    for line in f:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
    average_profit["average_profit"] = sum(profit.values()) / len(profit)
    list_full.append(profit)
    list_full.append(average_profit)
    print(list_full)

with open("data7.json", "w") as write_f:
    json.dump(list_full, write_f)
