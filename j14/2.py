n = int(input())

x = 0
if 1 <= n <= 100:
    for _ in range(1, n + 1):
        x += _

print(x)