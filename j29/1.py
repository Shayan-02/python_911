l = [1, 2, 3, 4, 5]
d = {1: "ali", 2: "reza", 3: "saeed", 4: "vahid", 5: "mohammad"}
t = (1, 2, 3, 4, 5)
s = "12345"
se = {1, 2, 3, 4, 5}

# int , float , bool ----------> nabayad bashad

for _ in l:
    if _ % 2 == 0:
        print(_, end="\t")
print()
for _ in d:
    if _ % 2 != 0:
        print(_, end="\t")
print()
for _ in t:
    if _ > 3:
        print(_, end="\t")
print()
for _ in se:
    if _ < 4:
        print(_, end="\t")
print()
for _ in s:
    if int(_) > 3:
        print(_, end="\t")
print()
