class Person:
    shakhs = "ensan"
    def __init__(self, name=None, sen=0):
        self.name = name
        self.sen = sen
    
    def sleep(self):
        return self.name + " خواب است"
    
    def moarefi(self):
        return f"{self.name} {self.sen} saal darad."


ali = Person("ali mohammadi", 20)
# print(ali.age)
print(ali.sen)
print(ali.moarefi())
