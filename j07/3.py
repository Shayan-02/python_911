c = 50

i = 5
while i:
    num = int(input("یک عدد حدس بزنید: "))
    if num == c:
        print("برنده شدی")
        break
    if num < c:
        print("عدد انتخاب شده کمتر از عدد درست است.")
    else:
        print("عدد انتخاب شده بزرگتر از عدد درست است.")
    i -= 1
else:
    print("باختی")
