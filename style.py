from random import randint

class TextRandom():
    def __init__(self, fontsize = [-5, 5], cursive = [-5, 5], thickness = [-1, 1], curl = [-5, 5]):
        self.fontsize = fontsize
        self.cursive = cursive
        self.thickness = thickness
        self.curl = curl

class TextStyle():
    def __init__(self, fontsize = 0, cursive = 5, thickness = 2, curl = 5, color = "#131315", random: TextRandom = None, xPos = 0, yPos = 0):
        self.fontsize = fontsize
        self.cursive = cursive
        self.thickness = thickness
        self.curl = curl
        self.color = color

        self.xPos = xPos
        self.yPos = yPos

        # random
        if random:
            self.random = random
        else:
            self.random = TextRandom()

        self.is_export = 1

    def set_export(self, value: bool):
        if value: 
            self.is_export = 2
        else:
            self.is_export = 1

    def rand(self, list_random):
        return randint(list_random[0], list_random[1]) * self.is_export

    def get_size(self):
        return (self.fontsize + self.rand(self.random.fontsize)) * self.is_export

    def get_cursive(self):
        return (self.cursive + self.rand(self.random.cursive)) * self.is_export

    def get_thickness(self):
        return (self.thickness + self.rand(self.random.thickness)) * self.is_export

    def get_curl(self):
        return (self.curl + self.rand(self.random.curl)) * self.is_export