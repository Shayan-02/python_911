from tkinter import *
class Shakhs:
    esm = "asghar"
    def sleep(self):
        return "یک شخص خوابیده است"
    def moarefi(self, name, age):
        return f"your name is {name} \nyour age is {age}"


p1 = Shakhs()
# print(p1.name, p1.age)
# print(p1.age)
print(p1.sleep())
print(p1.moarefi("reza", 25))

print("--------------------")

p2 = Shakhs()
print(p2.esm)
# print(p1.name, p1.age)
# print(p1.age)
print(p2.sleep())
print(p2.moarefi("mamad", 30))
