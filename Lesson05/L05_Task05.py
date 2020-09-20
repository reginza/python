# 4. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
import random
my_file = open(r'data5.txt', 'w')

my_list = [random.randint(0, 100) for i in range(10)]
print("Содержимое файла: ", my_list)
if my_file.writable():  # создание файла
    b = [str(x) for x in my_list]
    for i in b:
        my_file.write(i.replace('', ' '))
else:
    print("Can not write")

my_file = open(r'data5.txt')   # чтение файла
my_list_new = []
a = my_file.readline()
b = a.split()
b = ''.join(b)
for i in b:
    my_list_new.append(int(i))
print('Сумма чисел в чайле: ', sum(my_list_new))

my_file.close()
