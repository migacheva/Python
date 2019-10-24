# age = 20  # int(input("Введите возраст: "))
# sex = "F"  # str(input("Введите пол F/M: "))
# # print("Источник дохода:\n 1. Пассивный доход\n  2. Наёмный доход\n  3. Собственный бизнес\n  4. Безработный\n")
# sourceOfIncome = 2  # int(input("Введите источник дохода [1-4]: "))
# revenue = 3  # int(input("Введите годовой доход в млн: "))
# creditRating = 2  # int(input("Введите кредитный рейтинг [-2..2]: "))
# userLoan = 4  # int(input("Введите сумму запрашиваемого кредита в млн: "))
# deadline = 11  # int(input("Введите срок погашения [1..20] в годах: "))
# # print("Цели:\n 1. Ипотека\n 2. Развитие бизнеса\n 3. Автокредит\n 4. Потребительский\n")
# goal = 2  # int(input("Введите цель [1..4]: "))
#
# print(age, sex, sourceOfIncome, revenue, creditRating, userLoan, deadline, goal)



def sumLoan(sourceOfIncome, creditRating, userLoan):
    sourceOfIncome = float(sourceOfIncome)
    creditRating = float(creditRating)
    userLoan = float(userLoan)
    if sourceOfIncome == 1 or creditRating == -1:
        OkLoan = 1
        if userLoan <= OkLoan:
            print("кредит выдан")
        else:
            print("кредит не выдан (1)")
    elif sourceOfIncome == 2 or creditRating == 0:
        OkLoan = 5
        if userLoan <= OkLoan:
            print("кредит выдан")
        else:
            print("кредит не выдан (2)")
    elif (sourceOfIncome == 3 and (creditRating == 1 or creditRating == 2)) or (
            sourceOfIncome == 4 and (creditRating == 1 or creditRating == 2)):
        OkLoan = 10
        if userLoan <= OkLoan:
            print("кредит выдан")
        else:
            print("кредит не выдан по собственному доходу")


# print("1", sumLoan(1, -1, 0.5), " ==========")
# print("2", sumLoan(1, -1, 1.5), " ==========")
# print("3", sumLoan(1, 0,  0.5), " ==========")
# print("4", sumLoan(1, 0,  1.5), " ==========")
# print("5", sumLoan(1, 1, 0.5), " ==========")
# print("6", sumLoan(1, 1, 1.5), " ==========")
# print("7", sumLoan(1, 2, 0.5), " ==========")
# print("8", sumLoan(1, 2, 1.5), " ==========")
# print("9", sumLoan(2, -1, 0.5), " ==========")
# print("10", sumLoan(2, -1, 1.5), " ==========")
# print("11", sumLoan(2, 0, 4), " ==========")
# print("12", sumLoan(2, 0, 6), " ==========")
# print("13", sumLoan(2, 1, 4), " ==========")
# print("14", sumLoan(2, 1, 6), " ==========")
# print("15", sumLoan(2, 2, 4), " ==========")
# print("16", sumLoan(2, 2, 6), " ==========")
import math

print(-math.log10(10))