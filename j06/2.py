
for i in  range(30):
    num1 = int(input("enter number1: "))
    op = input("enter operator: ")
    num2 = int(input("enter number2: "))
    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        if num2 == 0:
            print("cannot divide by 0")
        else:
            print(num1 / num2)
    else:
        print("invalid operator")
    cont = input("do you want to continue? ")
    if cont == "n":
        break


print("edameh...")