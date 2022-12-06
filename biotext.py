# А Б В Г Ґ Д Е Є Ж З И І Ї Й К Л М 
#   Н О П Р С Т У Ф Х Ц Ч Ш Щ Ь Ю Я

# а б в г ґ д е є ж з и і ї й к л м 
#   н о п р с т у ф х ц ч ш щ ь ю я

from PyQt5.QtWidgets import QMainWindow, QApplication
from window import Ui_MainWindow

from PIL import Image, ImageDraw
from random import randint
import math


LARGE_UPCASES = ['Б', 'Г', 'Ґ', 'Д', 'Ж', 'И', 
                 'Й', 'М', 'О', 'П', 'У', 'Ф', 
                 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ю']

class TextDraw():
    def __init__(self, image: Image, fontsize = 50, thickness = 4, curl = [2, 5], cursive = 10, color = "red"):
        self.fontsize = fontsize
        self.curl = curl
        self.cursive = cursive
        self.thickness = thickness
        self.color = color
        self.canvas = ImageDraw.Draw(image);
        self.last_pos = []
        self.divide_random = [18, 22]

    def func(self, cords: list, t):
        new_cords = []
        for cord in cords:
            new_cords.append(((cord[0] * self.fontsize) / 50, (cord[1] * self.fontsize) / 50))

        cords = new_cords
        return (
            math.pow((1 - t), 3) * cords[0][0] + 3* math.pow((1-t), 2) * t * cords[1][0] + 3 * (1-t)*math.pow(t, 2) * cords[2][0] + math.pow(t, 3) * cords[3][0],
            math.pow((1 - t), 3) * cords[0][1] + 3* math.pow((1-t), 2) * t * cords[1][1] + 3 * (1-t)*math.pow(t, 2) * cords[2][1] + math.pow(t, 3) * cords[3][1]
        )
    
    def bezier(self, cords: list):
        for cord in cords:
            curve = []
            t = 0
            while (t < 1):
                curve.append(self.func(cord, t))
                t += 0.01

            while (t > 0):
                bezier = self.func(cord, t)
                curve.append((bezier[0], bezier[1] + math.pow(t + self.thickness, math.cos(t))))
                t -= 0.01

            self.last_pos = [curve[-1][0], curve[-1][1]]
            self.canvas.polygon(curve, self.color)

    def divide_func(self, xy: tuple, xy2: tuple, use_random = True):
        if use_random == 66:
            return ((xy[0] + xy2[0]) / (randint(self.divide_random[0], self.divide_random[1]) / 10), (xy2[0] + xy2[1]) / (randint(self.divide_random[0], self.divide_random[1]) / 10))
        else:
            return ((xy[0] + xy2[0]), (xy2[0] + xy2[1]))

    def divide(self, cords: list, divides):
        new_cords = []
        if divides > 0:
            for cord in cords:
                cords_list = []
                cords_list.append((cord[0][0], cord[0][1]))
                cords_list.append(self.divide_func(cord[0], cord[1]))
                cords_list.append((cord[1][0], cord[1][1]))
                cords_list.append(self.divide_func(cord[1], cord[2], False))
                cords_list[1] = (cords_list[1][0] + self.cursive, cords_list[1][1])
                cords_list[2] = (cords_list[2][0] + self.cursive, cords_list[2][1])

                new_cords.append(cords_list)

                cords_list = []
                cords_list.append(self.divide_func(cord[1], cord[2], False))
                cords_list.append((cord[2][0], cord[2][1]))
                cords_list.append(self.divide_func(cord[2], cord[3]))
                cords_list.append((cord[3][0], cord[3][1]))
                cords_list[1] = (cords_list[1][0] + self.cursive, cords_list[1][1])
                cords_list[2] = (cords_list[2][0] + self.cursive, cords_list[2][1])
                
                new_cords.append(cords_list)
                
            return self.divide(new_cords, divides-1)
        return cords


    # [[(25, 90), (45, 1), (55, 3), (65, 95)]]
    # [[(25, 90), (45, 1), (55, 3), (65, 95)], [(25, 90), (45, 1), (55, 3), (65, 95)]]

    def curve(self, cords: list, divide = 1):
        self.bezier(self.divide([cords], divide))

    def continue_(self, cords: list, divide = 1):
        cords[0][0] = self.last_pos[0]
        cords[0][1] = self.last_pos[1]
        self.curve(cords, divide)

    def draw(self, letter: str):
        if letter == 'A' or letter == 'А':
            self.curve([(25, 100), (20, 0), (80, 0), (75, 100)], 1)
            #self.curve([(0, 0), (2,5), (2,6), (2,6)])

class BioText(Ui_MainWindow, QMainWindow):
    def __init__(self, text: str, width = 500, height = 500): # offset max 3 elements
        super(Ui_MainWindow, self).__init__()
        self.ui = self.setupUi(self)

        self.strings = text;
        self.image = Image.new('RGBA', (width*2, height*2), (255, 255, 255, 255)) 
        self.text = TextDraw(self.image)

    def draw(self):
        self.text.draw(self.strings[0])
        self.image = self.image.resize((self.image.width // 2, self.image.height // 2), resample=Image.ANTIALIAS)