# 1. Создать программно файл в текстовом формате, записать
# в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

my_file = open(r'data1.txt', 'w')

user_text = 'SomeText'
while user_text != " ":
    if my_file.writable():
        user_text = input("Ведите данные (нажмите пробел для завершения ввода): ")
        my_file.write(user_text)

my_file.close()
