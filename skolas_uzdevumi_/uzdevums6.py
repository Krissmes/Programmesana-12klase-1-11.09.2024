import random
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
