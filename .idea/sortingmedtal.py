while True:
    try:
        sorting: int = int(input("Vælg en class. Tryk 1-5 for at vælge en af de forskellige type classes : "))
    except ValueError:
        print("ikke tilgænglig")
        continue
    print("Du har valgt:", sorting,)
    if sorting > 5 or sorting < 0:
        print("Du har valgt:", sorting,"Den class er ikke tilgænglig, prøv igen")
        continue
    break