num = int(input("enter a number: "))

if num > 0:
    print("positive")
    print("if block")
elif num < 0:
    print("negative")
    print("elif block")
else:
    print("zero")
    print("else block")