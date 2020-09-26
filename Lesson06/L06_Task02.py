# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна.
# Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т


class Road:
    length: int
    width: int
    height: int
    weight: int

    def __init__(self, length, width, height, weight):
        self.length = length
        self.width = width
        self.height = height
        self.weight = weight

    def massa(self):
        a = self.length * self.width * self.height * self.weight
        print(f"Формула для расчета массы асфальта: {self.length}м * {self.width}м * {self.height}см * "
              f"{self.weight}кг = {a}т")


v = Road(10, 11, 12, 2)


v.massa()
