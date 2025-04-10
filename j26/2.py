class Shakhs:
    def sleep(self, name):
        return f"{name} khaab ast"

    def moarefi(self, name, age):
        return f"your name is {name} \nyour age is {age}"

    def salam(self, name):
        return f"salam {name}"

    def bye(self, name):
        return f"khodahafez {name}"


s1 = Shakhs()
print(s1.sleep("ali"))
print(s1.moarefi("ali", 25))
print(s1.salam("ali"))
print(s1.bye("ali"))
