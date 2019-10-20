import math
# Задача-1: Написать класс для фигуры-треугольника,
# заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def lengAB(a, b):
    leng = math.sqrt((b[0] - a[0]) * (b[0] - a[0]) + (b[1] - a[1]) * (b[1] - a[1]))
    print("Длина отрезка: ", leng)
    return leng

class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        return self.perimeter(p1, p2, p3)

    def perimeter(self, p1, p2, p3):
        print("точечки треугольника", p1, p2, p3)
        lenp1p2 = lengAB(p1, p2)
        lenp2p3 = lengAB(p2, p3)
        lenp3p1 = lengAB(p3, p1)
        per = lenp1p2 + lenp2p3 + lenp3p1
        # print("Периметр треугольника", per)
        return per

    def square(self, a, b, c):
        p = (a+b+c)/2
        s = math.sqrt(p*(p-a)*(p-b)*(p-c))
        # print("Площадь: ", s)
        return s

# Пример использования класса треугольника:
tr_1 = Triangle((1, 2), (7, 9), (5, 0))
print(tr_1)
print('Площадь:', tr_1.square())
# print('Высота к стороне a:', tr_1.height_a())
# print('Высота к стороне b:', tr_1.height_b())
# print('Высота к стороне c:', tr_1.height_c())
print('Периметр:', tr_1.perimeter())


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы для:
#  - проверки, является ли фигура равнобочной трапецией;
#  - вычисления: длины сторон, периметр, площадь.

# Пример использования класса трапеции:
# class Trapezoid:
#     def __init__(self, p1, p2, p3, p4):
#         pass
#
# trap_1 = Trapezoid((0, 0), (1, 2), (3, 2), (4, 0))
# trap_2 = Trapezoid((0, 0), (1, 2), (3, 2), (6, 0))
# traps = [trap_1, trap_2]
#
# for trap in traps:
#     print(trap)
#     if trap.is_isosceles():
#         print('Равнобочная')
#     else:
#         print('Неравнобочная')
#     print('Длины сторон:', trap.sides())
#     print('Площадь:', trap.square())
#     print('Периметр:', trap.perimeter())
