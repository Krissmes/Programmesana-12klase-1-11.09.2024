dalamais = int(input("Ievadi skaitli no 1-100 un es tev pateikšu visus skaitļus ar ko viņš dalās."))
dalitajs = 1
while dalitajs != 101:
    if dalamais % dalitajs == 0:
        print(dalamais, "dalās ar", dalitajs)
        dalitajs +=1
    else:
        dalitajs +=1