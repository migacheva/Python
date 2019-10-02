#!/usr/bin/lessons
# -*- coding: utf-8 -*-
# задача 1
x = input("x:")
a = str(x)
counter = 0
print(a)
index = len(a) - 1
while counter <= index:
    print(a[counter])
    counter += 1
print("finished")
# задача 2
a = input("a: ")
b = input("b: ")
c = a
a = b
b = c
print ("a = ",a,"b = ",b)
# задача 3
q = int(input("Какой у вас возраст?"))
if q >= 18:
    print("Доступ разрешен")
else:
    print("Извините, доступ только с 18 лет, придется подождать")