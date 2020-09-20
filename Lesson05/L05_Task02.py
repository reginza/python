# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

my_file = open(r'data2.txt')

new_list = my_file.readlines()
b = [i.replace('\n', '') for i in new_list]
print(f'Содержимое файла: {b}')
print('Количество строк в файле:', len(new_list))

count = 1
for i in new_list:
    print('В', count, 'строке количество слов: ', len(i))
    count += 1

my_file.close()
