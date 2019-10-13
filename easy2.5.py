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
    path = os.getcwd() + "/" + name
    # for i in range(10):
    #     path = os.getcwd() + "/" + name + "/1"
    #     os.mkdirs(path)
    try:
        os.mkdir(path)
    except OSError:
        print ("Создать директорию %s не удалось" % path)
    else:
        print ("Успешно создана директория %s " % path)

def delete_dirs(name):
    path = os.getcwd() + "/" + name
    try:
        os.rmdir(path)
    except OSError:
        print ("Удалить директорию %s не удалось" % path)
    else:
        print ("Успешно удалена директория %s " % path)

create_dirs("newf")
delete_dirs("newf")

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
