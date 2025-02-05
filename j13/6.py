lst = []
for i in range(1, 11):
    if i % 2 == 0:
        lst.append(i**2)
print(lst)

print([i**2 for i in range(1, 11) if i % 2 == 0])

a = 10
b = 20

a, b = b, a
