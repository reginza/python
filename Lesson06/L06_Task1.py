# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и
# метод running (запуск). Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении
# выводить соответствующее сообщение и завершать скрипт.
import time


class TrafficLight:
    __color = str

    def running(self):
        self.color = red.color
        if red.__color:
            time.sleep(1)
            print(self.color)
        else:
            print(self.color)
        self.__color = yellow.color
        if red.__color:
            time.sleep(2)
            print(self.__color)
        else:
            print(self.color)
        self.color = green.color
        time.sleep(1)
        print(self.color)


red = TrafficLight()
yellow = TrafficLight()
green = TrafficLight()
a = TrafficLight()


red.color = "Red"
yellow.color = "Yellow"
green.color = "Green"


a.running()
