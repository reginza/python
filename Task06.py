km_day = float(input("Введите результат первого дня: "))
limit = float(input("Введите желаемый результат: "))
i = 1  # номер дня
print(f'1-й день: {km_day} км.')

while limit > km_day != 0:
    km_day = km_day + km_day * 0.1
    i = i + 1
    print(f'{i}-й день: {km_day:.2f} км.')
print(f'Ответ: на {i}-й день спортсмен достиг результата - не менее {limit:.2f} км.')
