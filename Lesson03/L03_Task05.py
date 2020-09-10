def user_number_sum(user_number):
    c = sum(user_number)
    print(c)
    elem_user_number = -1
    list_user_number = []
    list_user_number.append(c)
    while elem_user_number != 0:
        user_number = [int(i) for i in input("Введите числа через пробел. Для завершения введите число - 0 : ").split()]
        elem_user_number = min(user_number)
        b = sum(user_number)
        list_user_number.append(b)
        print(sum(list_user_number))
    if elem_user_number == 0:
        print("Программа завершена!")


user_number = [int(i) for i in input("Введите числа через пробел. Для завершения введите число - 0 : ").split()]
user_number_sum(user_number)
