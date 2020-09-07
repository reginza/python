rating = [7, 5, 3, 3, 2]
print(rating)

while True:
    b = int(input("Введите натуральное число: "))
    rating.append(b)
    d = sorted(rating, reverse=True)

    print("Пользователь ввел число", b, "Результат:: ", end="")
    print(*d, sep=", ")
