n = int(input("enter a number: "))
m = int(input("enter a number: "))

for i in range(1, n + 1): #sotun ha
    for j in range(1, m + 1): #satr ha
        print(i*j, end="\t")
    print()