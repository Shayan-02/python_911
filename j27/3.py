class Color:
    def __init__(self, rgb, name):
        self.rgb = rgb
        self.name = name

    def set_name(self, name):
        self.name = name
        
    def get_name(self):
        return self.name

    def set_rgb(self, rgb):
        self.rgb = rgb

    def get_rgb(self):
        return self.rgb


c = Color(0x6783F5, "light blue")
print(c.get_name())
print(c.get_rgb())
print(20 * "-")
c.set_rgb(0x091B66)
c.set_name("blue")
print(c.get_name())
print(c.get_rgb())
