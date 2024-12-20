a = 30
b = 20
c = 15

if a > b and a > c:
    print(f"a is the largest number-> {a}")
elif b > a and b > c:
    print("b is the largest number")
else:
    print("c is the largest number")

if a < b and a < c:
    print("a is the smallest number")
elif b < a and b < c:
    print("b is the smallest number")
else:
    print("c is the smallest number")


if a > b:
    if a > c:
        print("a is the largest number")
    else:
        print("c is the largest number")
elif b > a:
    if b > c:
        print("b is the largest number")
    else:
        print("c is the largest number")