c = 5

for i in range(3):
    num = int(input("Enter a number: "))
    if num == c:
        print("just right")
        break
    elif num < c:
        print("too low")
    else:
        print("too high")