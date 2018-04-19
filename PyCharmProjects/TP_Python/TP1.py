#!/usr/local/bin/python3
def exo1():
    for i in range(0, 500):
        print("Je dois faire des sauvegardes régulières de mes fichiers")


exo1()


def exo2():
    pair = []
    for a in range(0, 1000, 2):
        pair.append(a)
    print(pair)
    impair = [n + 1 for n in pair]
    print(impair)


exo2()


def exo3():
    for b in range(0, 10):
        print(b, "*", 13, "=", b * 13)


exo3()


def exo4():
    m = input("Enter a Word : ")
    print(len(m))


exo4()


def exo5():
    e = int(input("Enter a Number : "))
    if (e % 2) == 0:
        print("{0} est Pair".format(e))
    else:
        print("{0} est Impair".format(e))


exo5()
