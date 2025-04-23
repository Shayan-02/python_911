def test():
    global y
    y = 20
    return f"y -> {y}"


print(test())
print(y)
