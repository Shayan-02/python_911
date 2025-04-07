from random import *
def hadsKalameh():
    valid = ["Bedbug", "Bee", "Beetle", "Bird", "Bison", "Boa", "Boar", "Bobcat", "Bonobo", "Booby"]
    dorost = choice(valid)
    tedadshance = len(dorost)
    print(f"shoma {tedadshance} shance darid")
    for _ in range(tedadshance) :
        hads = input("entekhab: ")
        if hads == dorost:
            print("bordi")
            break
        else:
            print("eshtebah")
    else:
        print("bakhti")
hadsKalameh()
