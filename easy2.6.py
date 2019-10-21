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
    # print("Длина отрезка: ", leng)
    return leng


class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.a = lengAB(p1, p2)
        self.b = lengAB(p2, p3)
        self.c = lengAB(p3, p1)

    def perimeter(self):
        return self.a + self.b + self.c

    def square(self):
        p = (self.a + self.b + self.c) / 2
        s = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return s

    def height_a(self):
        p = (self.a + self.b + self.c) / 2
        ha = (2 * math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))) / self.a
        return ha

    def height_b(self):
        p = (self.a + self.b + self.c) / 2
        hb = (2 * math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))) / self.b
        return hb

    def height_c(self):
        p = (self.a + self.b + self.c) / 2
        hc = (2 * math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))) / self.c
        return hc


# Пример использования класса треугольника:
tr_1 = Triangle((1, 2), (7, 9), (5, 0))
# print(tr_1)
print('Площадь:', tr_1.square())
print('Высота к стороне a:', tr_1.height_a())
print('Высота к стороне b:', tr_1.height_b())
print('Высота к стороне c:', tr_1.height_c())
print('Периметр:', tr_1.perimeter())

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы для:
#  - проверки, является ли фигура равнобочной трапецией;
#  - вычисления: длины сторон, периметр, площадь.
# Пример использования класса трапеции:
class Trapezoid:
    def __init__(self, p1, p2, p3, p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.a = lengAB(p1, p2)
        self.b = lengAB(p2, p3)
        self.c = lengAB(p3, p4)
        self.d = lengAB(p4, p1)

    def is_isosceles(self):
        if self.a == self.c or self.b == self.d:
            return True

    def perimeter(self):
        return self.a + self.b + self.c + self.d

    def sides(self):
        return self.a, self.b, self.c, self.d

    def square(self):
        h = math.sqrt(self.a**2 - (((self.d - self.b)**2 + self.a**2 - self.c**2)/(2*(self.d - self.b)))**2)
        s = (self.d + self.b)*h/2
        return s



trap_1 = Trapezoid((0, 0), (1, 2), (3, 2), (4, 0))
trap_2 = Trapezoid((0, 0), (1, 2), (3, 2), (6, 0))
traps = [trap_1, trap_2]

print("трапецушки")
for trap in traps:
    # print(trap)
    if trap.is_isosceles():
        print('Равнобочная')
    else:
        print('Неравнобочная')
    print('Длины сторон:', trap.sides())
    print('Площадь:', trap.square())
    print('Периметр:', trap.perimeter())
