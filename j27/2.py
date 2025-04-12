class Daneshamooz:
    __classes = 101
    def __init__(self, esm, sen, maghta):
        self.esm = esm
        self.sen = sen
        self.maghta = maghta

    def gereftan_classes(self):
        global c
        c = int(input("class ra vared konid: "))
    
    def tanzim_classes(self):
        self.__classes = c
    
    def namayesh_classes(self):
        return self.__classes

d1 = Daneshamooz("ali", 15, 9)
print(d1.maghta)
d1.maghta = 10
print(d1.maghta)
# print(d1.__classes)

d1.gereftan_classes()
print("ghabl az tanzim: ")
print(d1.namayesh_classes())
d1.tanzim_classes()
print("baad az tanzim: ")
print(d1.namayesh_classes())
