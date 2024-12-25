import random as r
i = 3
s = r.randint(1, 10)
while i > 0:
    c = int(input(f"enter your choice. you have {i} chances: "))
    if c == s:
        print("just right")
        break
    elif c < s:
        print("too low")
    else:
        print("too high")
    i -= 1
else:
    print(s)