proceeds = float(input("Введите сумму выручки: "))
costs = float(input("Введите сумму издержки: "))
profit = proceeds - costs  # расчет прибыли
rent = profit / proceeds   # расчет рентабельности

if profit > 0:
    print(f'Вы работете в прибыль. Ваша рентабельность {rent:.2f}')
    people = int(input("Введите численность в фирме: "))
    profit_people = profit / people  # расчет прибыль фирмы в расчете на одного сотрудника
    print(f'Прибыль в расчете одного сотрудника {profit_people:.2f}')
elif profit == 0:
    print("Вы работете в 0")
else:
    print("Вы работете в убыток")
