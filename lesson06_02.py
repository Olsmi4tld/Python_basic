# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна.
# Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

        def calculate_mass(self, mass_1cm, layer_cm):
            return self._length * self._width * mass_1cm * layer_cm

road = Road(1, 2)
road.calculate_mass(3, 4)

# class Road:
#     def __init__(self, _length, _width):
#         self._length = _length
#         self._width = _width
#
#     def mass(self):
#         return self._length * self._width
#
#
# class MassCount(Road):
#     def __init__(self, _length, _width, volume):
#         super().__init__(_length, _width)
#         self.volume = volume
#
#
# r = MassCount(25, 10000, 125)
# print(r.mass())