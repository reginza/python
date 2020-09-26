# 5. Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.


class Mew:

    cat_name: str
    color: str
    age: int

    def mewmew(self):
        print(f'May cat: {self.cat_name}, {self.color}, {self.age} лет')


sims = Mew()
sims.cat_name = "Britain"
sims.color = "Grey"
sims.age = 10

print(sims.cat_name, sims.color, sims.age)
sims.mewmew()
