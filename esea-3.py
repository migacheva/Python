def task1():
    x = input("x:")
    a = str(x)
    counter = 0
    print (a)
    index = len(a) - 1
    while counter <= index:
        print (a[counter])
        counter += 1
    print ("finished")

task1()

def task2():
    a = input("a: ")
    b = input("b: ")
    c = a
    a = b
    b = c
    print ('a = ',a,'b = ',b)

#task2()


def task3():
    q = input("kakoy y vas vozrast? ")
    if q >= 18:
        print ("dostup razreshen")
    else:
        print ("izinite, dostup tolko s 18 let")

#task3()
