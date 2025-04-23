class Ensan:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job

    def goftanEtelaat(self):
        print(f"name : {self.name} \nage: {self.age}\njob: {self.job}")

    def harekat(self):
        pass


class DaneshAmooz(Ensan):
    def harekat(self):
        print("do pa rah miravad")


class Nozad(Ensan):
    def harekat(self):
        print("chahar dast o pa rah miravad")


d1 = DaneshAmooz("ali", 15, "maskhareh kardan")
n1 = Nozad("mamad", 1, "bazi kardan")

d1.goftanEtelaat()
n1.goftanEtelaat()
