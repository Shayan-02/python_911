for i in range(1, 201):
    if i == 100:
        continue
    print(i, end=" ")

print()
print()

x = 1
while x <= 200:
    if x == 100:
        x += 5
        continue
    print(x, end=" ")
    x += 1
