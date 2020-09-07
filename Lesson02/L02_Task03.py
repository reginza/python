number = input("Введите месяц в виде целого числа от 1 ло 12: ")
winter = {"1": "January", "2": "February", "12": "December"}
spring = {"3": "March", "4": "April", "5": "May"}
summer = {"6": "June", "7": "July", "8": "August"}
autumn = {"9": "September", "10": "October", "11": "November"}

if winter.get(number) != None: print("Зима")
elif spring.get(number) != None: print("Весна")
elif autumn.get(number) != None: print("Осень")
else:
    print("Лето")
