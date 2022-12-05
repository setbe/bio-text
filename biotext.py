# А Б В Г Ґ Д Е Є Ж З И І Ї Й К Л М 
#   Н О П Р С Т У Ф Х Ц Ч Ш Щ Ь Ю Я

# а б в г ґ д е є ж з и і ї й к л м 
#   н о п р с т у ф х ц ч ш щ ь ю я

from PIL import Image, ImageDraw
from random import randint
import math


LARGE_UPCASES = ['Б', 'Г', 'Ґ', 'Д', 'Ж', 'И', 
                 'Й', 'М', 'О', 'П', 'У', 'Ф', 
                 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ю']

class TextDraw():
    def __init__(self, image: Image, fontsize = 200, thickness = 4, curl = [2, 5], cursive = [4, 9], color = "red"):
        self.fontsize = fontsize
        self.curl = curl
        self.cursive = cursive
        self.thickness = thickness
        self.color = color
        self.canvas = ImageDraw.Draw(image);
        self.last_pos = []

    def bezier(self, cords: list, t):
        new_cords = []
        for cord in cords:
            new_cords.append((cord[0] * self.fontsize / 100, cord[1] * self.fontsize / 100))

        cords = new_cords
        
        return (
            math.pow((1 - t), 3) * cords[0][0] + 3* math.pow((1-t), 2) * t * cords[1][0] + 3 * (1-t)*math.pow(t, 2) * cords[2][0] + math.pow(t, 3) * cords[3][0],
            math.pow((1 - t), 3) * cords[0][1] + 3* math.pow((1-t), 2) * t * cords[1][1] + 3 * (1-t)*math.pow(t, 2) * cords[2][1] + math.pow(t, 3) * cords[3][1]
        )
    
    def curve(self, cords: list, divide = 1):
        curve = []
        t = 0
        while (t < 1):
            curve.append(self.bezier(cords, t))
            t += 0.01

        while (t > 0):
            bezier = self.bezier(cords, t)
            curve.append((bezier[0], bezier[1] + math.pow(t + self.thickness, math.cos(t))))
            t -= 0.01

        self.last_pos = [curve[-1][0], curve[-1][1]]
        self.canvas.polygon(curve, self.color)

    def draw(self, letter: str):
        if letter == 'A' or letter == 'А':
            self.curve([(25, 90), (45, 1), (55, 3), (65, 95)])

class Text():
    def __init__(self, text: str, width = 500, height = 500): # offset max 3 elements
        self.strings = text;
        self.image = Image.new('RGBA', (width*2, height*2), (0, 0, 0, 0)) 
        self.text = TextDraw(self.image)

    def draw(self):
        self.text.draw(self.strings[0])
        self.image = self.image.resize((self.image.width // 2, self.image.height // 2), resample=Image.ANTIALIAS)
        self.image.show()