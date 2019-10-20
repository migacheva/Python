import easy25
import os

# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

def abc():
    print("Выберите действие: \n"
      "1. Перейти в папку \n"
      "2. Просмотреть содержимое текущей папки \n"
      "3. Удалить папку \n"
      "4. Создать папку \n"
      "5. Выйти из программы"  )
    action = int(input())
    return action

running = True
while running:
    action = abc()
    path = os.getcwd()

    if action == 1:
        print("Переход в директорию")
        easy25.list_dir()
        name_dir = input("Введите наименование папки для перехода \n")
        try:
            content = os.chdir(name_dir)
            print("Содержимое папки: ", content)
        except OSError:
            print ("Мы успешно перешли")
    elif action == 2:
        print("Текущая папка состоит из:")
        easy25.list_dir()
    elif action == 3:
        print("Удаление папки")
        del_dir = input("Введите имя папки для удаления из списка выше \n")
        easy25.delete_dirs(del_dir)
    elif action == 4:
        print("Создание новой папки")
        new_dir = input("Введите имя папки \n")
        easy25.create_dirs(new_dir)
    elif action == 5:
        print("Выход из программы")
        running = False
    else:
        print("Введите действие от 1 до 4")

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
