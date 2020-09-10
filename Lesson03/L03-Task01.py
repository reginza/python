def division_r(x, y):
    try:
        return print(x / y)
    except ZeroDivisionError:
        return print("Ошибка: деление на ноль!")


a = int(input("Введите число: "))
b = int(input("Введите число: "))
division_r(a, b)
