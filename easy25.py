import os
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# определяем текущий каталог и печатаем
path = os.getcwd()
print("Текущая рабочая директория %s" % path)

def create_dirs9(name):
    # определим имя директории, которую создаём
    for i in range(1,10):
        path = os.getcwd() + "\\" + name + str(i)
        try:
            os.mkdir(path)
        except OSError:
            print ("Создать директорию %s не удалось" % path)
        else:
            print ("Успешно создана директория %s " % path)

def create_dirs(name):

    path = os.getcwd() + "\\" + name
    try:
        os.mkdir(path)
    except OSError:
        print ("Создать директорию %s не удалось" % path)
    else:
        print ("Успешно создана директория %s " % path)

def delete_dirs9(name):
    for i in range(1,10):
        path = os.getcwd() + "\\" + name + str(i)
        try:
            os.rmdir(path)
        except OSError:
            print ("Удалить директорию %s не удалось" % path)
        else:
            print ("Успешно удалена директория %s " % path)

def delete_dirs(name):
    path = os.getcwd() + "\\" + name
    try:
        os.rmdir(path)
    except OSError:
        print ("Удалить директорию %s не удалось" % path)
    else:
        print ("Успешно удалена директория %s " % path)

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def list_dir():
    print(os.listdir())

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
