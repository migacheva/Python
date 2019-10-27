#!/usr/bin/python3
import random

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html

"""


class Card:
    def __init__(self):
        self.line1 = []
        self.line2 = []
        self.line3 = []
        self.crossed = []

        while len(self.line1) < 9:
            i1 = random.randint(1, 30)
            i2 = random.randint(31, 60)
            i3 = random.randint(61, 90)
            self.line1.append(i1)
            self.line2.append(i2)
            self.line3.append(i3)

        i = random.sample(range(0, 9), 4)
        self.line1[i[0]] = None
        self.line1[i[1]] = None
        self.line1[i[2]] = None
        self.line1[i[3]] = None
        i = random.sample(range(0, 9), 4)
        self.line2[i[0]] = None
        self.line2[i[1]] = None
        self.line2[i[2]] = None
        self.line2[i[3]] = None
        i = random.sample(range(0, 9), 4)
        self.line3[i[0]] = None
        self.line3[i[1]] = None
        self.line3[i[2]] = None
        self.line3[i[3]] = None

    def print_card(self):
        print("--------------------------")
        self.print_line(self.line1)
        self.print_line(self.line2)
        self.print_line(self.line3)
        print("--------------------------")

    def print_line(self, line):
        formatted_line = ""
        for n in line:
            if n is None:
                formatted_line += "  "
            elif n in self.crossed:
                formatted_line += "--"
            else:
                formatted_line += "{:02d}".format(n)
            formatted_line += "|"
        print(formatted_line)

    def check_number(self, num):
        return num in self.line1 or num in self.line2 or num in self.line3

    def cross_num(self, num):
        self.cross_num_in_line(self.line1, num)
        self.cross_num_in_line(self.line2, num)
        self.cross_num_in_line(self.line3, num)

    def cross_num_in_line(self, line, num):
        for i in range(len(line)):
            if line[i] == num:
                self.crossed.append(num)



class Game:
    def __init__(self, my_card, pc_card, barrel_bag):
        self.my_card = my_card
        self.pc_card = pc_card
        self.barrel_bag = barrel_bag

    def start(self):
        game = True
        while game:
            print("Ваша карточка:")
            self.my_card.print_card()
            print("Карточка компьютера:")
            self.pc_card.print_card()

            current_barrel = self.barrel_bag.get_barrel()
            print("Вытащили бачонок: " + str(current_barrel))

            # Ход игрока
            answer = dialog("Зачеркнуть?")

            has_num = self.my_card.check_number(current_barrel)
            if answer:
                if not has_num:
                    print("Че ты врешь! Нет у тебя такого номера! Автолуз!")
                    game = False
            elif not answer:
                if has_num:
                    print("У тебя был такой номер! Внимательней будь, теперь тебе не выиграть!")
                    game = False
            else:
                print("Ниче не понял! (y/n)")
            self.my_card.cross_num(current_barrel)

            # Ход компьютера
            if self.pc_card.check_number(current_barrel):
                print("PC: Опа! Зачеркнул! :)")
                self.pc_card.cross_num(current_barrel)
            else:
                print("PC: У меня такого нет :(")

            # Итоги хода
            my_crossed = len(self.my_card.crossed)
            pc_crossed = len(self.pc_card.crossed)

            if my_crossed == 15 and pc_crossed == 15:
                print("Ничья")
                game = False
            elif my_crossed == 15 and pc_crossed < 15:
                print("Поздравляем! Вы виграли!")
                game = False
            elif my_crossed < 15 and pc_crossed == 15:
                print("Вы проиграли! Сорян...")
                game = False


class Barrel_bag:
    def __init__(self):
        self.barrels = list(range(1, 91))

    def get_barrel(self):
        rand_i = random.randint(0, len(self.barrels) - 1)
        rand_barrel = self.barrels[rand_i]
        self.barrels.remove(rand_barrel)
        return rand_barrel


def dialog(text):
    while True:
        req = input(text + " (y/n)")
        if req == "y":
            return True
        elif req == "n":
            return False
        else:
            print("Ниче не понял!")


new_game = Game(Card(), Card(), Barrel_bag())
again = True
while again:
    new_game.start()
    again = dialog("Поиграем еще?")