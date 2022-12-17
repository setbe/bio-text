from random import randint
from letter import load_handwriting

class TextRandom():
    def __init__(self, fontsize: list = [0, 0], cursive: list = [-5, 5], thickness: list = [0, 1], curl: list = [-2, 2]):
        self.fontsize = fontsize
        self.cursive = cursive
        self.thickness = thickness
        self.curl = curl

class TextStyle():
    def __init__(self, fontname: str = "standard", fontsize: int = 48, cursive: int = 10, thickness: int = 2, curl: int = 2, color = "#131315", random: TextRandom = None, xPos: int = 0, yPos: int = 0):
        self.set_font(fontname)
        self.fontsize = fontsize
        self.cursive = cursive
        self.thickness = thickness
        self.curl = curl
        self.color = color

        self.xPos = xPos
        self.yPos = yPos
        self.random = random if random else TextRandom()

        self.local_curl = 0

    def rand(self, list_random):
        return randint(list_random[0], list_random[1])

    def get_size(self):
        return self.fontsize + self.rand(self.random.fontsize)

    def get_cursive(self):
        return self.cursive + self.rand(self.random.cursive)

    def get_thickness(self):
        return self.thickness + self.rand(self.random.thickness)

    def get_curl(self):
        try:
            return self.rand([self.random.curl[0] - self.curl - self.local_curl, self.random.curl[1] + self.curl + self.local_curl])
        except:
            return self.rand([-1, 1])

    def set_font(self, fontname):
        self.font = load_handwriting(fontname, py_file=True)