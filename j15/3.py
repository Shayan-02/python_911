def jam(a, b):
    return a + b


def tafrigh(a, b):
    return a - b


def zarb(a, b):
    return a * b


def taghsim(a, b):
    return a / b


num1 = int(input("enter first number: "))
op = input("enter a operator: ")
num2 = int(input("enter second number: "))

if op == "+":
    print(jam(num1, num2))
elif op == "-":
    print(tafrigh(num1, num2))
elif op == "*":
    print(zarb(num1, num2))
elif op == "/":
    print(taghsim(num1, num2))
