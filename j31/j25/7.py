num1 = input("enter number1: ")
op = input("enter an operator: ")
num2 = input("enter number2: ")

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    try:
        print(int(num1) / int(num2))
        print(n)
    # except ZeroDivisionError:
    #     print("can't devide by zero")
    # except ValueError:
    #     print("inputs must be base 10")
    except Exception as e:
        print(e)
print("continue")
