a = [2, 32, 4, 15, 23, 1, 0]

# a.sort(reverse=True)
a.reverse()
print(a)
b = a.copy()
print(b)
a.clear()
print(a)
print(b)
a = b.copy()
print(a)