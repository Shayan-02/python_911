def ichapkon():
    for i in range(1, 11):
        yield i


x = ichapkon()
for i in x:
    print(i)
