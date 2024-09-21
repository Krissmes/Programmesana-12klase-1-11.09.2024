
def fibonaci():
    x = 1
    y = 0
    z = 0
    summa = 0
    while z <= int(4000000):
        for i in range(1,40):
            z = x + y
            x = y
            y = z
            print(summa)
            # if z >= int(4000000):
            #     print(summa)
            # el
            if z % 2 == 0:
                summa += z
    print(summa)
fibonaci()


