import math

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n,m):
    if m < 0:
        print("Введите положительные значения")
    elif m == 0:
        print([1])
    elif m == 1:
        print([1,1])
    else:
        f = [None] * m
        f[0] = 1
        f[1] = 1
        for i in range(2, m):
            f[i] = f[i-1]+f[i-2]
        print("task #1 ", f[n:m])
fibonacci(11,23)

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(origin_list):
    print("task #2 не отсортированный список", origin_list)
    for i in range(len(origin_list)-1):
        for j in range(len(origin_list) - 1):
            if origin_list[j] > origin_list[j+1]:
                k = origin_list[j]
                origin_list[j] = origin_list[j+1]
                origin_list[j + 1] = k
    print("task #2 отсортированный список", origin_list)

sort_to_max([2, 10, -12, 10 , 10, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
def new_filter(func, iter):
    for i in iter:
        if func(i):
            yield i # Аналог return
print("task #3 отрицательные числа и ноль", list(new_filter(lambda x: x<=0, [1, -4, 0, 45, 78, 0, -4, -9])))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

a1x = 1 #int(input("Координаты X т.1 "))
a1y = 1 #int(input("Координаты Y т.1 "))
a2x = 0 #int(input("Координаты X т.2 "))
a2y = 3 #int(input("Координаты Y т.2 "))
a3x = 1 #int(input("Координаты X т.3 "))
a3y = 5 #int(input("Координаты Y т.3 "))
a4x = 2 #int(input("Координаты X т.4 "))
a4y = 3 #int(input("Координаты Y т.4 "))
x = [a1x, a2x, a3x, a4x]
y = [a1y, a2y, a3y, a4y]
a12 = math.sqrt((a1x-a2x)**2 + (a1y-a2y)**2)
a23 = math.sqrt((a2x-a3x)**2 + (a2y-a3y)**2)
a34 = math.sqrt((a3x-a4x)**2 + (a3y-a4y)**2)
a41 = math.sqrt((a4x-a1x)**2 + (a4y-a1y)**2)

if a12 == a34 and a23 == a41:
    print("task #4 ", "Параллелограм")
else:
    print("task #4 ", "нет")
