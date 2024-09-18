vards = input("izvēlies vārdu.")
burts = input("izvēlies burtu un es pateikšu cik daudz tas burts ir iekšā tajā vārdā.")
skaits=0
for x in vards:
    if x == burts:
        skaits += 1
print(skaits)