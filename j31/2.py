num1 = input("enter num1: ")
op = input("enter an operator: ")
num2 = input("enter num2: ")

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    try:
        print(int(num1) / int(num2))
    except Exception as e:
        print(e)
    finally:
        print("edameh")
