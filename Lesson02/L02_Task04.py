words = [i for i in input("Введите несколько слов через пробел: ").split()]
count = 1
word_in_list = ""
for i in range(0, len(words)):
    word_in_list = words[i]
    print(count, word_in_list[0:10])
    count += 1
