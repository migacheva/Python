import math


age1 = 20
sex1 = "F"
sourceOfIncome1 = 2 # print("Источник дохода:\n 1. Пассивный доход\n  2. Наёмный доход\n  3. Собственный бизнес\n  4. Безработный\n")
revenue1 = 3
creditRating1 = 2
userLoan1 = 4
deadline1 = 11
goal1 = 2  # print("Цели:\n 1. Ипотека\n 2. Развитие бизнеса\n 3. Автокредит\n 4. Потребительский\n")


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

def changeBasePer(goal, creditRating, sourceOfIncome, userLoan):
    if goal:
        if goal == 1:
            per = -2
        elif goal == 2:
            per = -0.5
        elif goal >= 3:
            per = 1.5
    if creditRating:
        if creditRating == -1:
            per = per + 1.5
        elif creditRating == 0:
            per = 0
        elif creditRating == 1:
            per = per - 0.25
        elif creditRating == 2:
            per = per - 0.75
    if sourceOfIncome:
        if sourceOfIncome == 1:
            per = per + 0.5
        elif sourceOfIncome == 2:
            per = per - 0.25
        elif sourceOfIncome == 3:
            per = per + 0.25
    if userLoan:
        modifikator = -math.log10(userLoan)
        per = per + modifikator
    # print("modifikator", modifikator)
    # print("4%", per)
    return per

def getLoan(age, sex, sourceOfIncome, revenue, creditRating, userLoan, deadline, goal):
    if ((age + deadline) != 60 and sex == "F") or ((age + deadline) != 65 and sex == "M") and (age >= 18):
        print("1. Возраст ок")
        if (userLoan / deadline) < (revenue / 3):
            print("2. Запрашиваемая сумма/срок погашения меньше трети дохода")
            if creditRating != -2:
                print("3. Кредитный рейтинг ок")
                if sourceOfIncome != 4:
                    print("4. Клиент не безработный")
                    changeBasePerQQ = changeBasePer(goal, creditRating, sourceOfIncome, userLoan)
                    basePer = 10
                    yearPayWithPers = (userLoan * (1 + deadline * (basePer + changeBasePerQQ) / 100)) / deadline
                    print("Годовой платеж с процентами = ", yearPayWithPers)
                    if yearPayWithPers < revenue / 2:
                        print("5. Годовой платеж с проценами менее половины дохода")
                        sumLoan(sourceOfIncome, creditRating, userLoan)
                        # print("Посчитанные процентыыыы", changeBasePer(goal, creditRating, sourceOfIncome, userLoan))
                        print("========= Проверки завершены  =========")
                        # if sumLoanQQ:
                        #     print("Сумма платежа соответствует - 6")
                        # else:
                        #     print("Кредит НЕ выдан - 6")
                    else:
                        print("Кредит НЕ выдан, т.к. годовой платеж с проценами более половины дохода (5)")
                        print("========= Проверки завершены  =========")
                else:
                    print("Кредит НЕ выдан, т.к. клиент безработный (4)")
                    print("========= Проверки завершены  =========")
            else:
                print("Кредит НЕ выдан, т.к. кредитный рейтинг -2 (3)")
                print("========= Проверки завершены  =========")
        else:
            print("Кредит НЕ выдан, т.к. запрашиваемая сумма/срок погашения более трети дохода (2)")
            print("========= Проверки завершены  =========")
    else:
        print("Кредит НЕ выдан, т.к. возраст либо мал, либо велик (1)")
        print("========= Проверки завершены  =========")



      # age, sex, sourceOfIncome, revenue, creditRating, userLoan, deadline, goal
getLoan(18,  "M",       2,           3,         1,          4,          1,      1)
getLoan(10, "M", 2, 3, 1, 4, 1, 1)
getLoan(80, "F", 2, 3, 1, 4, 9, 1)
getLoan(55, "M", 2, 3, 1, 4, 5, 1)
