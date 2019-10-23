import math

age = 20  # int(input("Введите возраст: "))
sex = "F"  # str(input("Введите пол F/M: "))
# print("Источник дохода:\n"
#       "1. Пассивный доход\n"
#       "2. Наёмный доход\n"
#       "3. Собственный бизнес\n"
#       "4. Безработный\n")
sourceOfIncome = 2  # int(input("Введите источник дохода [1-4]: "))
revenue = 3  # int(input("Введите годовой доход в млн: "))
creditRating = 2  # int(input("Введите кредитный рейтинг [-2..2]: "))
userLoan = 4  # int(input("Введите сумму запрашиваемого кредита в млн: "))
deadline = 11  # int(input("Введите срок погашения [1..20] в годах: "))
# print("Цели:\n"
#       "1. Ипотека\n"
#       "2. Развитие бизнеса\n"
#       "3. Автокредит\n"
#       "4. Потребительский\n")
goal = 2  # int(input("Введите цель [1..4]: "))

# ЗАГЛУШКА ДЛЯ СЛЕД МЕТОДА
yearPayWithPer = 15
loan = False
print(age, sex, sourceOfIncome, revenue, creditRating, userLoan, deadline, goal)


def getLoan(age, sex, sourceOfIncome, revenue, creditRating, userLoan, deadline):
    print("Посчитанные процентыыыы", changeBasePer(goal, creditRating, sourceOfIncome, userLoan))
    if ((age + deadline) != 60 and sex == "F") or ((age + deadline) != 65 and sex == "M") or (age >= 18):
        print("1. Возраст ок")
        if (userLoan / deadline) < (revenue / 3):
            print("2. Запрашиваемая сумма/срок погашения меньше трети дохода")
            if creditRating != -2:
                print("3. Кредитный рейтинг ок")
                if sourceOfIncome != 4:
                    print("4. Клиент не безработный")
                    # Заглушка!!!!!
                    yearPayWithPer = 1
                    if yearPayWithPer < revenue / 2:
                        print("5. Годовой платеж с проценами менее половины дохода")
                        if sumLoan(sourceOfIncome, creditRating, userLoan):
                            print("Сумма платежа соответствует - 6")
                        else:
                            print("Кредит НЕ выдан - 6")
                            print("sourceOfIncome-", sourceOfIncome, "creditRating-", creditRating, "userLoan-", userLoan)
                    else:
                        print("Кредит НЕ выдан - 5")
                else:
                    print("Кредит НЕ выдан - 4")
            else:
                print("Кредит НЕ выдан - 3")
        else:
            print("Кредит НЕ выдан - 2")
    else:
        print("Кредит НЕ выдан - 1")


# Проверка на сумму кредита
def sumLoan(sourceOfIncome, creditRating, userLoan):
    # Проверка по источнику дохода
    if sourceOfIncome == 1:
        # userLoan должен быть <= 1млн
        if userLoan <= 1:
            print("6.1 источнику дохода ok")
        else:
            print("кредит не выдан по пассивному доходу")
    elif sourceOfIncome == 2:
        # userLoan должен быть <= 5млн
        if userLoan <= 5:
            print("6.2 источник дохода ok")
        else:
            print("кредит не выдан по наёмному доходу")
    elif sourceOfIncome == 3:
        # userLoan должен быть <= 10млн
        if userLoan <= 10:
            print("6.3 источник дохода ok")
        else:
            print("кредит не выдан по собственному доходу")
    # Проверка по рейтингу
    elif creditRating == -1:
        if userLoan <= 1:
            print("6.4 кредитный рейтинг ok")
        else:
            print("кредит не выдан по рейтингу -1")
    elif creditRating == 0:
        if userLoan <= 5:
            print("кредитный рейтинг ok")
        else:
            print("6.5 кредит не выдан по рейтингу 0")
    elif creditRating >= 1:
        if userLoan <= 10:
            print("6.6 кредитный рейтинг ok")
        else:
            print("кредит не выдан по рейтингу 1 или 2")
#     Написать проверку по минимальному условию!! (т.е. если источник дохода - собственный, а рейтинг 0 - то вычисляем)

def basePer():
    base = 10
    yearPayWithPer = (sumLoan() * (1 + deadline * (base + changeBasePer())/100))/deadline
    print(yearPayWithPer)

def changeBasePer(goal, creditRating, sourceOfIncome, userLoan):
    if goal:
        if goal == 1:
            per = -2
        elif goal == 2:
            per = -0.5
        elif goal >= 3:
            per = 1.5
    # print("1%", per)
    if creditRating:
        if creditRating == -1:
            per = per + 1.5
        elif creditRating == 0:
            per = 0
        elif creditRating == 1:
            per = per -0.25
        elif creditRating == 2:
            per = per -0.75
    # print("2%", per)
    if sourceOfIncome:
        if sourceOfIncome == 1:
            per = per + 0.5
        elif sourceOfIncome == 2:
            per = per -0.25
        elif sourceOfIncome == 3:
            per = per + 0.25
    # print("3%", per)
    if userLoan:
        modifikator = -math.log(userLoan)
        per = per + modifikator
    # print("modifikator", modifikator)
    # print("4%", per)
    return per


getLoan(age, sex, sourceOfIncome, revenue, creditRating, userLoan, deadline)
