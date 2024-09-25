import time
import random
def uzdevums1(vards,uzvards,vecums,dzivosanasVieta,milakaisPrieksmets):
        
    # vards = str(input('Kā tevi sauc?'))
    # uzvards = str(input('Kāds ir tavs uzvārds?'))
    # vecums = int(input('Cik tevi gadi?'))
    # dzivosanasVieta = str(input('Kur tu dzīvo?'))
    # milakaisPrieksmets = str(input('Kas ir tavs mīļākais priekšmets?'))
    time.sleep(2)
    print("Es tagad varu nozagt tavu identitāti :)")

    time.sleep(3)

    print("Mani sauc", vards)
    time.sleep(1)
    print("Mans uzvārds ir", uzvards)
    time.sleep(1)
    print("Man ir", vecums , 'gadi')
    time.sleep(1)
    print("Es dzīvoju", dzivosanasVieta)
    time.sleep(1)
    print("Mans mīļākais priekšmets ir", milakaisPrieksmets)

def uzdevums2():
    pvn = 0.79
    cenaArPvn = int(input('Cik maksāja pirkums?'))
    cenaBezPvn = pvn*cenaArPvn
    print("Jūsu cena bez pvn ir", cenaBezPvn )
def uzdevums3():
    yearNow = 2024
    yearUser = int(input("Kurā gadā esi dzimis?"))
    if yearNow - yearUser > 18:
        print("Tevi ir vairāk par 18 gadiem. Nice!")
    else:
        print("Tevi ir 18 vai mazāk gadu. Ir vēl kur augt.")
def uzdevums4():
    "yes"
def uzdevums5():
    atbilde = str(input("Gribi atkārtot programmu?y/n---"))
    while atbilde == str("y") :
        atbilde = str(input("Gribi atkārtot programmu?y/n---"))
    if atbilde == str("n"):
        print("Ok, beigšu strādāt.")
    else :
        print("Es nesadarbojos ar cilvēkiem, kas nemāk rakstīt.")
def uzdevums6():
    
    uzminamais = random.randint(1,10)
    atbilde = int(input("Uzmini ciparu no 1-10?"))
    while uzminamais != atbilde:
        if uzminamais > atbilde:
            print("Cipars ir lielāks")
            atbilde = int(input("Uzmini ciparu no 1-10?"))
        if uzminamais < atbilde:
            print("Cipars ir mazāks")
            atbilde = int(input("Uzmini ciparu no 1-10?"))
    if uzminamais == atbilde:
        print("Tu uzminēji, cipars bija", uzminamais)

def uzdevums7():
    dalamais = int(input("Ievadi skaitli no 1-100 un es tev pateikšu visus skaitļus ar ko viņš dalās."))
    dalitajs = 1
    while dalitajs != 101:
        if dalamais % dalitajs == 0:
            print(dalamais, "dalās ar", dalitajs)
            dalitajs +=1
        else:
            dalitajs +=1
def uzdevums8():
    vards = input("izvēlies vārdu.")
    burts = input("izvēlies burtu un es pateikšu cik daudz tas burts ir iekšā tajā vārdā.")
    skaits=0
    for x in vards:
        if x == burts:
            skaits += 1
    print(skaits)    
def uzdevums9():
    summa = 0
    for x in range(1,1000):
        if x % 3 == 0:
            summa += x
        elif x % 5 == 0:
            summa += x
    print(summa)
def uzdevums10():
    "fibonaci"
def uzdevums11():
    visiBurti= "abcdefghijklmnopqrstuvwxyz"
    for y in visiBurti:
        for x in visiBurti:
            print (y,x)
def uzdevums12():
    n = int(input())
    atbilde = 2**n
    print(atbilde)
uzdevums1("hellp","hello","18","riga","matematika")