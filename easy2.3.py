# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

# number1 = input("введите чиселку: ")
# ndigits1 = input("введите, до коле округлять будем: ")
def my_round(number, ndigits):
    # number = str(number)
    # ndigits = str(ndigits)
    # if ("." in number) and ("." not in ndigits):
    #     print("посмотрим, что тут у нас")
    #     dot_index = number.find(".")
    #     index_round = dot_index + int(ndigits)
    #     print("позиция округления", index_round)
    #     whole_part = number[0:dot_index]
    #     print("кусок целой части", whole_part)
    #     fractional_part = number[dot_index+1:index_round+1]
    #     print("кусок дробной части", fractional_part)
    #     len_fractional = len(str(fractional_part))
    #     if len_fractional <= int(ndigits):
    #         # добить нулями
    #         fractional_part = fractional_part + "0"
    #         print("дробная часть с нулями", fractional_part)
    #     if int(number[index_round]) < 4:
    #         # обрезаем до позиции r
    #         fractional_part = fractional_part[0:index_round]
    #         print("не требуется округление", fractional_part)
    #     else:
    #         # обрезаем до r
    #         fractional_part = fractional_part[0:index_round]
    #         # добавляем 1
    #         fractional_part = fractional_part[0:-2] + str(int(fractional_part[-1]) + 1)
    #         print("Округлили", fractional_part)
    #     # если новая длина стала больше
    #         # увеличить целую часть
    #     all_num = whole_part + "." + fractional_part
    #     print(all_num)
    # else:
    #     print("параметры некорректные или округлять нечего")
    res = '{:.{}}'.format(number, ndigits)
    print("Task #1", res)
my_round(0.23999, 4)
my_round(0.339999, 1)

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

# не совсем понимаю, почему не нужно выводить результаты проверки, заменила на True/False

ticket_number = input("Введите номер билета: ")
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
