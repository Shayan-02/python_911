import time
class Shakhs:
    # class
    # property
    # init
    # method
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sleep(self):
        return f"{self.name} khaab ast"

    def moarefi(self):
        return f"your name is {self.name} \nyour age is {self.age}"

    def salam(self):
        return f"salam {self.name}"

    def bye(self):
        return f"khodahafez {self.name}"


s1 = Shakhs("ali", 20)
print(s1.sleep())
print(s1.salam())
print(s1.moarefi())
print(s1.bye())
print("-----------------")
print("moshakhasat dar hal e tagheer ast...")
time.sleep(10)
s1.name = "mohammad"
s1.age = 18

print("moshkhasat tagheer kard...")
print(s1.sleep())
print(s1.salam())
print(s1.moarefi())
print(s1.bye())
