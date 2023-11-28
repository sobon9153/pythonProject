import math

print("witaj\npomogę Ci rozwiązać zadanie geodezyjne zwykłe \noraz zadanie geodezyjne otwarte")

print("Powiedz który typ zadania chcesz rozwiązać ZGZ czy ZGO")

while True:
    rodzaj = input(":").upper()
    if rodzaj == 'ZGZ':
        print("wybrałeś ZGZ")
        while True:
            try:
                azymut = int(input("Podaj azymut T z punktu do punktu B zapis podaj w całości bez przecinków: "))
                break
            except ValueError:
                print("podana nieprawidłowa wartość, spróbuj jeszcze raz")
        while True:
            try:
                odleglosc = int(input("Podaj odległość między punktem A i punktem B:"))
                break
            except ValueError:
                print("podana nieprawidłowa wartość, spróbuj jeszcze raz")
        print("przejdziemy teraz do współrzędnych prostokątnych\n"
              "PAMIĘTAJ aby współrzędne podać w zapisie 5 cyfrowym np 39620 lub 39600\n"
              "zależy od Ciebie z jaką dokładności chcesz pracować")

        azymut_w_stopniach = azymut * 0.06
        przyrost_rzedna = math.sin(math.radians(azymut_w_stopniach))
        przyrost_odcieta = math.cos(math.radians(azymut_w_stopniach))
        przyrost_A = przyrost_rzedna * odleglosc
        przyrost_B = przyrost_odcieta * odleglosc

        while True:
            rzedna_A = input("Podaj rzędną współrzędnych prostokątnych punktu A: ")
            if len(rzedna_A) == 5 and rzedna_A.isdigit():
                rzedna_A = float(rzedna_A)
                break
            else:
                print("spróbuj jeszcze raz, podaj dokładnie 5 liczb")

        while True:
            odcieta_A = input("Podaj odciętą współrzędnych prostokątnych punktu A: ")
            if len(odcieta_A) == 5 and odcieta_A.isdigit():
                odcieta_A = float(odcieta_A)
                break
            else:
                print("spróbuj jeszcze raz, podaj dokładnie 5 cyfr")

        rzedna_B = rzedna_A + przyrost_A
        odcieta_B = odcieta_A + przyrost_B
        print("azymut w stopniach:{:.2f}".format(azymut_w_stopniach))
        print("przyrost rzędna:{:.2f}".format(przyrost_A))
        print("przyrost odcięta:{:.2f}".format(przyrost_B))
        print("rzedna B:{:.0f}".format(rzedna_B))
        print("odcięta B:{:.0f}".format(odcieta_B))
        break
    elif rodzaj == 'ZGO':
        print("wybrałeś ZGO")

        while True:
            rzedna_A1 = input("Podaj rzędną współrzędnych prostokątnych punktu A: ")
            if len(rzedna_A1) == 5 and rzedna_A1.isdigit():
                rzedna_A1 = float(rzedna_A1)
                break
            else:
                print("spróbuj jeszcze raz, podaj dokładnie 5 liczb")

        while True:
            odcieta_A1 = input("Podaj odciętą współrzędnych prostokątnych punktu A: ")
            if len(odcieta_A1) == 5 and odcieta_A1.isdigit():
                odcieta_A1 = float(odcieta_A1)
                break
            else:
                print("spróbuj jeszcze raz, podaj dokładnie 5 cyfr")

        while True:
            rzedna_B1 = input("Podaj rzędną współrzędnych prostokątnych punktu B: ")
            if len(rzedna_B1) == 5 and rzedna_B1.isdigit():
                rzedna_B1 = float(rzedna_B1)
                break
            else:
                print("spróbuj jeszcze raz, podaj dokładnie 5 liczb")

        while True:
            odcieta_B1 = input("Podaj odciętą współrzędnych prostokątnych punktu B: ")
            if len(odcieta_B1) == 5 and odcieta_B1.isdigit():
                odcieta_B1 = float(odcieta_B1)
                break
            else:
                print("spróbuj jeszcze raz, podaj dokładnie 5 cyfr")
        przyrost_rzedna1 = rzedna_B1 - rzedna_A1
        przyrost_odcieta1 = odcieta_B1 - odcieta_A1
        dowolna = przyrost_rzedna1 / przyrost_odcieta1
        dowolna = abs(dowolna)
        tan_roznicy_przyrostu = math.atan(dowolna)
        azymutZGO = tan_roznicy_przyrostu / 0.06
        print("Przyrost E", przyrost_rzedna1)
        print("przyrost N", przyrost_odcieta1)
        print("tangens", tan_roznicy_przyrostu)
        print("azymut przed czwartakiem:{:.2f}".format(azymutZGO))
        if przyrost_rzedna1 > 0 and przyrost_odcieta1 > 0:
            print("Azymut na punktu A do punktu B to:{:.2f}".format(azymutZGO))
        elif przyrost_rzedna1 > 0 > przyrost_odcieta1:
            a = 30.00 - azymutZGO
            print("Azymut na punktu A do punktu B to:{:.2f}".format(a))
        elif przyrost_rzedna1 < 0 and przyrost_odcieta1 < 0:
            b = 30.00 + azymutZGO
            print("Azymut na punktu A do punktu B to:{:.2f}".format(b))
        elif przyrost_rzedna1 < 0 < przyrost_odcieta1:
            c = 60.00 - azymutZGO
            print("Azymut na punktu A do punktu B to:{:.2f} ".format(c))

        odleglosc_AB = math.sqrt(przyrost_rzedna1 ** 2 + przyrost_odcieta1 ** 2)
        print("odległość z punktu A do punktu B:{:.2f} ".format(odleglosc_AB))
        break
    else:
        print("podaj poprawną wartość ZGZ albo ZGO")