import exam_prog


def meow_test(actual, expected):
    if actual == expected:
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Тест пройден")
    else:
        print("-------------------------------------------------------------------- Тест провален")


# age, sex, sourceOfIncome, revenue, creditRating, userLoan, deadline, goal
# #Проверка на возраст не ок
meow_test(exam_prog.getLoan(17, "M", 2, 3, 1, 4, 1, 1), "возраст либо мал, либо велик (1)")  # не ок
meow_test(exam_prog.getLoan(65, "M", 2, 3, 1, 4, 1, 1), "возраст либо мал, либо велик (1)")
meow_test(exam_prog.getLoan(60, "F", 2, 3, 1, 4, 1, 1), "возраст либо мал, либо велик (1)")
meow_test(exam_prog.getLoan(-5, "F", 2, 3, 1, 4, 1, 1), "возраст либо мал, либо велик (1)")
# Проверка на возраст ок
meow_test(exam_prog.getLoan(51, "F", 2, 3, 1, 4, 9, 1), "кредит выдан")
meow_test(exam_prog.getLoan(18, "F", 2, 3, 1, 4, 5, 1), "кредит выдан")
meow_test(exam_prog.getLoan(60, "M", 2, 3, 1, 4, 5, 1), "кредит выдан")

# # Запрашиваемая сумма/срок погашения меньше/равна/больше трети дохода userLoan/deadline < revenue/3
meow_test(exam_prog.getLoan(18, "F", 2, 3, 1, 4, 5, 1), "кредит выдан")  # ок
meow_test(exam_prog.getLoan(18, "F", 2, 3, 1, 5, 5, 1),
          "запрашиваемая сумма/срок погашения более или равен трети дохода (2)")  # не ок
meow_test(exam_prog.getLoan(18, "F", 2, 3, 1, 6, 5, 1),
          "запрашиваемая сумма/срок погашения более или равен трети дохода (2)")  # не ок

# Кредитный рейтинг -2
meow_test(exam_prog.getLoan(18, "F", 2, 3, -2, 4, 5, 1), "кредитный рейтинг -2 (3)")  # не ок

# источник дохода = безработный
meow_test(exam_prog.getLoan(18, "F", 4, 3, 2, 4, 5, 1), "клиент безработный (4)")  # не ок

# годовой платеж с процентами </=/> половины дохода  yearPayWithPers </=/> revenue/2
meow_test(exam_prog.getLoan(18, "F", 2, 3, 1, 4, 5, 1), "кредит выдан")
meow_test(exam_prog.getLoan(18, "F", 2, 2.1518352006937632, 1, 4, 5, 1),
          "запрашиваемая сумма/срок погашения более или равен трети дохода (2)")
meow_test(exam_prog.getLoan(18, "F", 2, 2, 1, 4, 5, 1),
          "запрашиваемая сумма/срок погашения более или равен трети дохода (2)")

# Проверки на доступную сумму кредита
meow_test(exam_prog.sumLoan(1, -1, 0.5), "кредит выдан")
meow_test(exam_prog.sumLoan(1, -1, 1.5), "кредит не выдан")
meow_test(exam_prog.sumLoan(1, 0, 0.5), "кредит выдан")
meow_test(exam_prog.sumLoan(1, 0, 1.5), "кредит не выдан")
meow_test(exam_prog.sumLoan(1, 1, 0.5), "кредит выдан")
meow_test(exam_prog.sumLoan(1, 1, 1.5), "кредит не выдан")
meow_test(exam_prog.sumLoan(1, 2, 0.5), "кредит выдан")
meow_test(exam_prog.sumLoan(1, 2, 1.5), "кредит не выдан")
meow_test(exam_prog.sumLoan(2, -1, 0.5), "кредит выдан")
meow_test(exam_prog.sumLoan(2, -1, 1.5), "кредит не выдан")
meow_test(exam_prog.sumLoan(2, 0, 4), "кредит выдан")
meow_test(exam_prog.sumLoan(2, 0, 6), "кредит не выдан")
meow_test(exam_prog.sumLoan(2, 1, 4), "кредит выдан")
meow_test(exam_prog.sumLoan(2, 1, 6), "кредит не выдан")
meow_test(exam_prog.sumLoan(2, 2, 4), "кредит выдан")
meow_test(exam_prog.sumLoan(2, 2, 6), "кредит не выдан")

# Проверка вычислений платежа с процентами 0.7203620447913259
meow_test(exam_prog.getLoan(51, "F", 2, 3, 1, 4, 9, 1), "кредит выдан")
