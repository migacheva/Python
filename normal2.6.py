# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

# Подсказка: обратите внимание на примеры в директории examples.


class School:
    def __init__(self, groups):
        self.groups = groups


class StudentsGroup:
    def __init__(self, name, students, teachers, subjects):
        self.name = name
        self.students = students
        self.teachers = teachers
        self.subjects = subjects


class Student:
    def __init__(self, name, mom, dad):
        splitted = name.split()
        self.firstname = splitted[0]
        self.secondname = splitted[1]
        self.othetname = splitted[2]
        self.mom = mom
        self.dad = dad
        self.group = None

    def set_group(self, group):
        self.group = group

    def get_name_parents(self):
        return self.mom + ' и ' + self.dad

    def formatted_name(self):
        let1 = self.secondname[0]
        let2 = self.othetname[0]
        return self.firstname + ' ' + let1 + '.' + let2 + '.'

class Teacher:
    def __init__(self, name, subjects):
        self.name = name
        self.subject = subjects


st1 = Student("Иванов Иван Иванович", "Иванова Раиса", "Иванов Иван")
st2 = Student("Петров Петр Петрович", "Петрова Раиса", "Петров Петр")
st3 = Student("Васильев Василий Васильевич", "Васильева Василиса", "Васильев Василий")
st4 = Student("Дмитров Дмитрий Дмитриевич", "Дмитрова Василиса", "Дмитров Дмитрий")
st5 = Student("Андреев Андрей Андреевич", "Андреева Василиса", "Андреев Андрей")
st6 = Student("Ваничкин Ванечка Ваничкович", "Ваничкина Василиса", "Ваничкин Ванечка")
st7 = Student("Артемов Артем Артемовив", "Артемова Василиса", "Артемов Артем")
st8 = Student("Алексеев Алексей Алексеевич", "Алексеева Алиса", "Алексеев Алексей")
st9 = Student("Александрова Александра Александровна", "Александрова Василиса", "Александров Александр")
st10 = Student("Радионов Радион Радионович", "Радионова Раиса", "Радионов Радион")

list_st_1A = [st9, st10]
list_st_9A = [st1, st2, st3, st8]
list_st_9B = [st4, st5, st6, st7]

tech1 = Teacher("Косогорова Светлана Юрьевна", "биология")
tech2 = Teacher("Азон Роман Владимирович", "информатика")
tech3 = Teacher("Кушпита Дмитрий Юрьевич", "Труды")
tech4 = Teacher("Комарова Елена Николаевна", "Алгебра")
tech5 = Teacher("Николаева Елена Николаевна", "Алгебра")
tech6 = Teacher("Буткова Наталья рудольфовна", "химия")
tech7 = Teacher("Сомова Анна Николаевна", "химия")

list_tech_1A = [tech1, tech3, tech2]
list_tech_9A = [tech1, tech7, tech2, tech4]
list_tech_9B = [tech1, tech6, tech2, tech5]

list_subj_1A = ["обж", "физра", "труды"]
list_subj_9A = ["биология", "Химия", "Информатика", "Геометрия"]
list_subj_9B = ["биология", "Химия", "Информатика", "Алгебра"]

gr1 = StudentsGroup("1А", list_st_1A, list_tech_1A, list_subj_1A)
gr2 = StudentsGroup("9А", list_st_9A, list_tech_9A, list_subj_9A)
gr3 = StudentsGroup("9Б", list_st_9B, list_tech_9B, list_subj_9B)

st1.set_group(gr2)
st2.set_group(gr2)
st3.set_group(gr2)
st4.set_group(gr3)
st5.set_group(gr3)
st6.set_group(gr3)
st7.set_group(gr3)
st8.set_group(gr2)
st9.set_group(gr1)
st10.set_group(gr1)

list_gr = [gr1, gr2, gr3]

print("1. Получить полный список всех классов школы")
school = School(list_gr)
for grp in school.groups:
    print(grp.name)

print("2. Получить список всех учеников в указанном классе")
for st in gr3.students:
    print(st.formatted_name())

print("3. Получить список всех предметов указанного ученика")
for tech in st1.group.teachers:
    print(tech.subject)

print("4. Узнать ФИО родителей указанного ученика")
print(st9.get_name_parents())

print("5. Получить список всех Учителей, преподающих в указанном классе")
for tech in gr3.teachers:
    print(tech.name)