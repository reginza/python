usertime = int(input("Введите время в секундах: "))
hours = usertime // 3600
minutes = (usertime // 60) - (hours * 60)
seconds = usertime % 60

print(f'{hours:02}:{minutes:02}:{seconds:02}')
