# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

# number1 = input("введите чиселку: ")
# ndigits1 = input("введите, до коле округлять будем: ")
number1 = str(0.23939)
ndigits1 = str(4)
def my_round(number, ndigits):
# Разделение целой и дробной части
    if ("." in number) and ("." not in ndigits):
        print("посмотрим, что тут у нас")
        print("округлим: ", number)
        dot_index = number.find(".")
        print("позиция точки ", dot_index)
        index_round = dot_index + int(ndigits)
        print("позиция округления", index_round)
        whole_part = number[0:dot_index]
        print("кусок целой части", whole_part)
        fractional_part = number[dot_index+1:index_round+1]
        print("кусок дробной части", fractional_part)
        len_fractional = len(str(fractional_part))
        if int(number[index_round+1]) > 4:
            new_fractional_part = int(fractional_part) + 1
            print("увеличили дробную часть, стало: ", new_fractional_part)
            new_len_fractional = len(str(new_fractional_part))
            if int(len_fractional) < new_len_fractional:
                print("Увеличилась длина дробной части")
                whole_part = int(whole_part) + 1
                print("Целая часть стала: ", whole_part)
                print("надо привести в порядок длину дробной части")
                new_fractional_part = str(new_fractional_part)[1:int(new_fractional_part)+1]
                if int(len(new_fractional_part)) == len_fractional:
                    print("длина корректная")
            whole_number = str(whole_part) + "." + str(new_fractional_part)
            print("округленное число", whole_number)
#        elif int(number[index_round+1]) is None:
#            print("Не на что смотреть для округления, думаю как реализовать")
        else:
            print("дробную часть не увеличиваем")
            whole_number = str(whole_part) + "." + str(fractional_part)
            print("округленное число", whole_number)
    else:
        print("параметры некорректные или округлять нечего")

my_round(number1, ndigits1)


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

# не совсем понимаю, почему не нужно выводить результаты проверки, заменила на True/False

# ticket_number = input("Введите номер билета: ")
ticket = str("123123")
def lucky_ticket(ticket_number):
    part_one = ticket_number[0:3]
    part_two = ticket_number[3:6]
    sum_part_one = int(part_one[0]) + int(part_one[1]) + int(part_one[2])
    sum_part_two = int(part_two[0]) + int(part_two[1]) + int(part_two[2])
    if len(ticket_number) == 6:
        if sum_part_one == sum_part_two:
#            print("Билет счастливый")
            return True
    else:
#        print("билет не ок")
        return False
#    print(sum_part_one, sum_part_two)
lucky_ticket(ticket)
