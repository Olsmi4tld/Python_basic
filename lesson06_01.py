# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера,
# создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.

from itertools import cycle
from time import sleep

class TrafficLight:
    __colors = {'red': 7, 'yellow': 2, 'green': 7}

    def running(self, run_count):
        colors_iteration = cycle(TrafficLight.__colors)
        while run_count:
            current_light_value = next(colors_iteration)
            print(f'The signal is: {current_light_value}')
            sleep(TrafficLight.__colors[current_light_value])
            run_count -= 1

traffic_light = TrafficLight()
traffic_light.running(10)
#
# from time import sleep
#
# class TrafficLight:
#     __color = ['Красный', 'Желтый', 'Зеленый']
#
#     def running(self):
#         i = 0
#         while i < 3:
#             print(f'Светофор переключается \n '
#                   f'{TrafficLight.__color[i]}')
#             if i == 0:
#                 sleep(7)
#             elif i == 1:
#                 sleep(5)
#             elif i == 2:
#                 sleep(3)
#             i += 1
#
#
# TrafficLight = TrafficLight()
# TrafficLight.running()