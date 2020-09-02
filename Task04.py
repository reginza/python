num_user = int(input("Введите число: "))
current_max = 0  # максимально число
num_cons = 0  # перемення для остатка от деления по модулю

while num_user > 0:
    num_cons = num_user % 10
    if num_cons > current_max:
        current_max = num_cons
    else:
        current_max = current_max
    num_user = num_user // 10

print("Максимльное число:", current_max)
