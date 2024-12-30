start = int(input("شروع بازه: "))
end = int(input("پایان بازه: "))

for _ in range(start, end+1):
    if _ % 3 == 0 and _ % 5 != 0:
        if _ == 42 or _ == 57 or _ == 69:
            continue
        print(_, end=" ")
