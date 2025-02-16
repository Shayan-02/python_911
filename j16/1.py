def test(n):
    valid = []
    for i in range(1, (n // 2) + 1):
        if n % i == 0:
            valid.append(i)
    if sum(valid) == n:
        return "YES"
    else:
        return "NO"


n = int(input())
print(test(n))