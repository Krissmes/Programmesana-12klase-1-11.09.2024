
def fibonaci():
    x = 0
    y = 1
    z = 1
    summa = 0
    while z <= int(4000000):
            z = x + y
            x = y
            y = z
            print(summa)
            if z % 2 == 0:
                summa += z
    print(summa)
fibonaci()


