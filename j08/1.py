sums, count = 0, 0
r = 1
while r:
    ans = int(input("enter a number: "))
    if ans == 0:
        r = 0
    else:
        sums += ans
        count += 1

avg = sums / count
print(avg)