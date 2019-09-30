#!/usr/bin/lessons
# -*- coding: utf-8 -*-
import math
# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4
a = input("a")
b = input("b")
c = input("c")
d= (b*b)-4*(a*c)
if d<0:
    print ("нет решения")
elif d==0:
    x0=(-b)/2*a
    print ("есть один корень", x0)
else:
    x1 = (-b + math.sqrt(d))/(2*a)
    x2 = (-b - math.sqrt(d))/(2*a)
    print ('x1', x1, 'x2', x2)