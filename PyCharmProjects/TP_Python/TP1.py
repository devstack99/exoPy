#!/usr/local/bin/python3
def exo1():
    for i in range(0, 500):
        print("Je dois faire des sauvegardes régulières de mes fichiers")


exo1()


def exo2():
    pair = []
    for a in range(0, 1000, 2):
        pair.append(a)
    print(pair, pair, sep='\n- ')
    impair = [n + 1 for n in pair]
    print(impair,impair, sep='\n- ')


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
    print('Exo Pair/Impair')
    e = int(input("Enter a Number : "))
    if (e % 2) == 0:
        print("{0} est Pair".format(e))
    else:
        print("{0} est Impair".format(e))


exo5()

"""

def exo6():
    num = int((input("Enter A number Between 10 and 20 : ")))
    if num > 20:
        print('Plus Petit ! ')
        exo6()
    if num < 10:
        print("Plus Grand ! ")
        exo6()
    if num >= 10:
            print("Yuppi ! ")
    if num =< 20:
        print("Yuppi ! ")


exo6()
"""


def exo07():
    seq = int(input(' Enter A Number : '))
    for a in range(seq, seq + 10):
        print(a + 1)


exo07()


def exo08():
    b = input("Enter A Number : ")
    for i in range(0, 10):
        print(b, "*", i, "=", int(b) * int(i))


exo08()



def exo09():
    num = int(input("Enter A Number : "))
    x = 0
    bri = 1
    while num > bri:
     x = (x + bri)
     bri = bri+1
    print(x)

exo09()

def exo10():
    age = int(input("Enter An Age : "))
    poussin: range = range(6, 7)
    pupille: range = range(8, 9)
    pinime: range = range(10, 11)
    cadet: range = range(12)
    if age in poussin:
        print("Tu est Un : Poussin")
    if age in pupille:
        print("Tu est Un : Pupille")
    if age in pinime:
        print("Tu est Un : Pinime")
    if age in cadet:
        print("Tu est Un : Cadet")
    else:
        print("Try Again!!!")
        exo10()

exo10()

def exo11():
    articles = int(input("Combien D'Articles : "))
    prix_ht = int(input("Enter Your Price : "))
    prix_ht_total = int((prix_ht * articles))
    tax = int(prix_ht_total * 0.20)
    prix_ttc = int(prix_ht_total) + int(tax)
    print("you Have ", articles, " Articles")
    print(prix_ht_total, " €")
    print("Le Prix TTC Total est De : ", prix_ttc, "€")

exo11()