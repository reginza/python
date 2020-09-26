# 6. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
# Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение. Создать экземпляры классов и
# проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:
    title: str

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки - {self.title}')


class Pen(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Вы взяли {self.title}. Запуск отрисовки')


class Pencil(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Вы взяли {self.title}. Запуск отрисовки')


class Handle(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Вы взяли {self.title}. Запуск отрисовки')


a = Pen("Ручка")
b = Pencil("Карандаш")
c = Handle("Маркер")

a.draw()
b.draw()
c.draw()
