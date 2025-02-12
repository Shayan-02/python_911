def test():
    global a, b
    a = 50 # global
    b = 100 # global
    c = 150 # local
    return a

print(test())
print(a, b)