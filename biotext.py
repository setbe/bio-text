# А Б В Г Ґ Д Е Є Ж З И І Ї Й К Л М 
#   Н О П Р С Т У Ф Х Ц Ч Ш Щ Ь Ю Я

# а б в г ґ д е є ж з и і ї й к л м 
#   н о п р с т у ф х ц ч ш щ ь ю я

from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap, QImage
import PyQt5.QtCore as QtCore
from PyQt5.QtCore import QBuffer
from window import Ui_MainWindow
import io

from PIL import Image, ImageDraw, ImageFilter
from PIL.ImageQt import ImageQt
from random import randint
import math
import functools


LARGE_UPCASES = ['Б', 'Г', 'Ґ', 'Д', 'Ж', 'И', 
                 'Й', 'М', 'О', 'П', 'У', 'Ф', 
                 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ю']

class TextDraw():
    def __init__(self, image: Image, fontsize = 550, thickness = 4, curl = [2, 5], cursive = 10, color = "red"):
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

    def curve(self, cords: list, divide = 0):
        self.bezier(self.divide([cords], divide))

    def continue_(self, cords: list, divide = 0):
        cords[0][0] = self.last_pos[0]
        cords[0][1] = self.last_pos[1]
        self.curve(cords, divide)

    def draw(self, letter: str):
        if letter == 'A' or letter == 'А':
            self.curve([(25, 100), (20, 0), (80, 0), (75, 100)])
            #self.curve([(0, 0), (2,5), (2,6), (2,6)])
    
    def clear(self, image: Image):
        self.canvas.rectangle((0, 0, image.width, image.height), fill=(0, 0, 0, 0))

class BioText(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.ui = self.setupUi(self)
        self.source_image = None        # QPixmap          // user image
        self.source_pil = None
        self.overlay_image = None       # Pillow Image     // where text will be rendered
        self.obj = None                 # TextDraw Class   // text render class

        # connections / signals
        self.textEdit.textChanged.connect(self.text_changed)
        # source image (AKA user image)
        self.lImage.mousePressEvent = self.open_image
        self.lImage.resizeEvent = self.resize_source_image
        # actions
        self.actionExport.triggered.connect(self.export)
        self.actionQuit.triggered.connect(self.quit)
        self.actionText.triggered.connect(self.save_text)

        # spinboxes -- Style
        
        # spinboxes -- Text
        self.sXPos.valueChanged.connect(self.x_pos_value_changed)
        self.sYPos.valueChanged.connect(self.y_pos_value_changed)

    def redraw_overlay(self):
        if self.source_image and not self.source_image.isNull():
            self.obj.clear(self.overlay_image)
            if self.textEdit.toPlainText():
                self.obj.draw(self.textEdit.toPlainText().split("\n")[0][0])

            source = self.source_pil

            overlay = self.overlay_image.resize((self.overlay_image.width // 2, self.overlay_image.height // 2), resample=Image.ANTIALIAS)
            source.paste(overlay, (self.sXPos.value(), self.sYPos.value()), overlay)
            source = ImageQt(source)

            pixmap = QPixmap.fromImage(source)
            pixmap = pixmap.scaled(self.lImage.width(), self.lImage.height(), QtCore.Qt.KeepAspectRatio)
            self.lImage.setPixmap(pixmap)

    def open_image(self, event):
        if not self.source_image or self.source_image.isNull():
            imagePath, _ = QFileDialog.getOpenFileName()
            if imagePath:
                self.source_image = QPixmap(imagePath)
                if not self.source_image.isNull():
                    self.source_pil = QPixmap.toImage(self.source_image)
                    buffer = QBuffer()
                    buffer.open(QBuffer.ReadWrite)
                    self.source_pil.save(buffer, 'PNG')
                    self.source_pil = Image.open(io.BytesIO(buffer.data()))
                    self.overlay_image = Image.new('RGBA', (self.source_image.width()*2, self.source_image.height()*2), (0, 0, 0, 0)) 
                    self.obj = TextDraw(self.overlay_image)
                    self.resize_source_image(0)
    
    def resize_source_image(self, event):
        if self.source_image:
            self.redraw_overlay()

    def export(self):
        if self.source_image and self.overlay_image:
            imagePath, _ = QFileDialog.getSaveFileName(self,"Export to...","","png;;jpg;;gif;;bpm;;jpeg;;webp")
            if imagePath:
                self.obj.clear(self.overlay_image)
                if self.textEdit.toPlainText():
                    self.obj.draw(self.textEdit.toPlainText().split("\n")[0][0])

                    source = self.source_pil
                    overlay = self.overlay_image
                    overlay = overlay.resize((self.overlay_image.width // 2, self.overlay_image.height // 2), resample=Image.ANTIALIAS)
                    overlay = overlay.filter(ImageFilter.SMOOTH)

                    source.paste(overlay, (self.sXPos.value(), self.sYPos.value()), overlay)
                    _ = _.strip()
                    if _ in ['jpg', 'jpeg', 'bmp']:
                        source = source.convert('RGB')
                    source.save(imagePath + "." + _)

    def save_text(self):
        if self.textEdit.toPlainText():
            f = open("text.txt", "w")
            f.write(self.textEdit.toPlainText())
            f.close()

    def quit(self):
        self.close()

    def text_changed(self):
        self.redraw_overlay()

    def value_changed(method):
        @functools.wraps(method)
        def wrapper(self):
            method(self)
            self.redraw_overlay()
        return wrapper

    # spinboxes
    @value_changed
    def fontsize_value_changed(self):
        pass

    @value_changed
    def cursive_value_changed(self):
        pass

    @value_changed
    def thickness_value_changed(self):
        pass

    @value_changed
    def thickness_value_changed(self):
        pass

    @value_changed
    def x_pos_value_changed(self):
        pass

    @value_changed
    def y_pos_value_changed(self):
        pass

    @value_changed
    def thickness_value_changed(self):
        pass

    @value_changed
    def resolution_width_value_changed(self):
        pass

    @value_changed
    def resolution_height_value_changed(self):
        pass

    @value_changed
    def anchor_x1_value_changed(self):
        pass

    @value_changed
    def anchor_y1_value_changed(self):
        pass

    @value_changed
    def anchor_x2_value_changed(self):
        pass

    @value_changed
    def anchor_y2_value_changed(self):
        pass

    @value_changed
    def anchor_x3_value_changed(self):
        pass

    @value_changed
    def anchor_y3_value_changed(self):
        pass

    @value_changed
    def anchor_x4_value_changed(self):
        pass

    @value_changed
    def anchor_y4_value_changed(self):
        pass