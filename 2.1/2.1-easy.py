#!/usr/bin/lessons
# -*- coding: utf-8 -*-
# задача 1
x = input("x:")
a = str(x)
counter = 0
print (a)
index = len(a) - 1
while counter <= index:
    print (a[counter])
    counter += 1
print ("finished")