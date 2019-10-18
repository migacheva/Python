import os
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# определяем текущий каталог и печатаем
path = os.getcwd()
print("Текущая рабочая директория %s" % path)

def create_dirs(name):
    # определим имя директории, которую создаём
    for i in range(1,10):
        path = os.getcwd() + "\\" + name + str(i)
        try:
            os.mkdir(path)
        except OSError:
            print ("Создать директорию %s не удалось" % path)
        else:
            print ("Успешно создана директория %s " % path)

def delete_dirs(name):
    for i in range(1,10):
        path = os.getcwd() + "\\" + name + str(i)
        try:
            os.rmdir(path)
        except OSError:
            print ("Удалить директорию %s не удалось" % path)
        else:
            print ("Успешно удалена директория %s " % path)

# create_dirs("dir")
# delete_dirs("dir")

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def list_dir():
    print(os.listdir())

list_dir()
# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
