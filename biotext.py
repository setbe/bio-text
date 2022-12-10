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


class TextStyle():
    def __init__(self, fontsize = 0, cursive = 5, thickness = 2, curl = 5, color = "#131315"):
        self.fontsize = fontsize
        self.cursive = cursive
        self.thickness = thickness
        self.curl = curl
        self.color = color

        self.xPos = 0
        self.yPos = 0

class TextDraw():
    def __init__(self, style: TextStyle):
        self.im = None
        self.canvas = None
        self.last_pos = []
        self.divide_random = [18, 22]
        if style:
            self.style = style
        else:
            self.style = TextStyle()

    def func(self, cords: list, t):
        new_cords = []
        for cord in cords:
            new_cords.append(((cord[0] * self.style.fontsize) / 50, (cord[1] * self.style.fontsize) / 50))

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
                curve.append((bezier[0], bezier[1] + math.pow(t, math.cos(t))))
                t -= 0.01

            self.last_pos = [curve[-1][0], curve[-1][1]]
            self.canvas.polygon(curve, self.style.color)

    def divide_func(self, xy: tuple, xy2: tuple, use_random = True, xy3_4 = None):
        if use_random == 66:
            return ((xy[0] - xy2[0]) / (randint(self.divide_random[0], self.divide_random[1]) / 10), (xy2[1] - xy2[1]) / (randint(self.divide_random[0], self.divide_random[1]) / 10))
        else:
            if xy3_4 == None:
                return ((xy[0] + xy2[0]) / 2, (xy2[1] + xy2[1]) / 2)
            else:
                return ((xy[0] + xy2[0]) / 2 - ((xy3_4[0] + xy3_4[0]) / 2) / 2, (xy2[1] + xy2[1]) / 2 - ((xy3_4[1][1] + xy3_4[1][1]) / 2) / 2)

    def divide(self, cords: list, divides):
        new_cords = []
        if divides > 0:
            for cord in cords:
                cords_list = []
                cords_list.append((cord[0][0], cord[0][1]))
                cords_list.append(self.divide_func(cord[0], cord[1]))
                cords_list.append((cord[1][0], cord[1][1]))
                cords_list.append(self.divide_func(cord[1], cord[2]))
                cords_list[2] = (cords_list[2][0] + self.style.cursive, cords_list[2][1])
                cords_list[3] = (cords_list[3][0] + self.style.cursive, cords_list[3][1])

                new_cords.append(cords_list)

                cords_list = []
                cords_list.append(self.divide_func(cord[1], cord[2]))
                cords_list.append((cord[2][0], cord[2][1]))
                cords_list.append(self.divide_func(cord[2], cord[3]))
                cords_list.append((cord[3][0], cord[3][1]))
                cords_list[0] = (cords_list[0][0] + self.style.cursive, cords_list[0][1])
                cords_list[1] = (cords_list[1][0] + self.style.cursive, cords_list[1][1])
                
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
        w = len(max(letter.split('\n'))) * self.style.fontsize
        h = len(letter.split('\n')) * self.style.fontsize

        self.im = Image.new("RGBA", (w*2, h*2), color=(0,0,0,0))
        self.canvas = ImageDraw.Draw(self.im, "RGBA")

        if letter == 'A' or letter == 'А':
            self.curve([(35, 90), (24, 15), (70, 10), (65, 90)], 1)
            #self.curve([(0, 0), (2,5), (2,6), (2,6)])
        self.im = self.im.resize((w, h), Image.ANTIALIAS)
        return self.im

class BioText(Ui_MainWindow, QMainWindow):
    def __init__(self, text_style: TextStyle = None):
        super(Ui_MainWindow, self).__init__()
        self.ui = self.setupUi(self)
        self.source_image = None        # QPixmap          // user image
        self.source_pil = None
        self.draw = TextDraw(text_style)                 # TextDraw Class   // text render class
        
        if text_style:
            self.sSize.setValue(text_style.fontsize)
            self.sCursive.setValue(text_style.cursive)
            self.sThickness.setValue(text_style.thickness)
            self.sCurl.setValue(text_style.curl)

            self.sXPos.setValue(text_style.xPos)
            self.sYPos.setValue(text_style.yPos)

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
        self.sSize.valueChanged.connect(self.fontsize_changed)
        self.sCursive.valueChanged.connect(self.spinbox_changed)
        self.sThickness.valueChanged.connect(self.thickness_changed)
        self.sCurl.valueChanged.connect(self.curl_changed)

        self.sSizeMin.valueChanged.connect(self.spinbox_changed)
        self.sSizeMax.valueChanged.connect(self.spinbox_changed)
        self.sCursiveMin.valueChanged.connect(self.spinbox_changed)
        self.sCursiveMax.valueChanged.connect(self.spinbox_changed)
        self.sThicknessMin.valueChanged.connect(self.spinbox_changed)
        self.sThicknessMax.valueChanged.connect(self.spinbox_changed)
        self.sCurlMin.valueChanged.connect(self.spinbox_changed)
        self.sCurlMax.valueChanged.connect(self.spinbox_changed)
        self.sDivide.valueChanged.connect(self.spinbox_changed)
        
        # spinboxes -- Text
        self.sXPos.valueChanged.connect(self.xPos_changed)
        self.sYPos.valueChanged.connect(self.yPos_changed)
        self.sWidth.valueChanged.connect(self.spinbox_changed)
        self.sHeight.valueChanged.connect(self.spinbox_changed)
        self.ax1.valueChanged.connect(self.spinbox_changed)

    def redraw_overlay(self):
        if self.source_image and not self.source_image.isNull():
            if self.textEdit.toPlainText():
                overlay = self.draw.draw(self.textEdit.toPlainText().split("\n")[0][0])
                source = self.source_pil.copy()
                source.paste(overlay, (self.sXPos.value(), self.sYPos.value()), overlay)
                source = ImageQt(source)

                pixmap = QPixmap.fromImage(source)
                pixmap = pixmap.scaled(self.lImage.width(), self.lImage.height(), QtCore.Qt.KeepAspectRatio)
                self.lImage.setPixmap(pixmap)

    def open_image(self, event = None, path = None):
        if not self.source_image or self.source_image.isNull():
            if not path:
                imagePath, _ = QFileDialog.getOpenFileName()
            else:
                imagePath = path
            if imagePath:
                self.source_image = QPixmap(imagePath)
                if not self.source_image.isNull():
                    self.source_pil = QPixmap.toImage(self.source_image)
                    buffer = QBuffer()
                    buffer.open(QBuffer.ReadWrite)
                    self.source_pil.save(buffer, 'PNG')
                    self.source_pil = Image.open(io.BytesIO(buffer.data()))
                    if self.draw.style.fontsize == 0:
                        self.draw.style.fontsize = self.source_pil.height // 20
                        self.sSize.setValue(self.draw.style.fontsize)
                    self.resize_source_image()
    
    def resize_source_image(self, event = None):
        if self.source_image:
            self.redraw_overlay()

    def export(self):
        if self.source_image and self.textEdit.toPlainText():
            imagePath, _ = QFileDialog.getSaveFileName(self,"Export to...","","png;;jpg;;gif;;bpm;;jpeg;;webp")

            if imagePath:
                overlay = self.draw.draw(self.textEdit.toPlainText().split("\n")[0][0])
                source = self.source_pil
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
            try: 
                method(self)
                self.redraw_overlay()
            except:
                pass
        return wrapper

    @value_changed
    def spinbox_changed(self):
        pass

    @value_changed
    def fontsize_changed(self):
        self.draw.style.fontsize = self.sSize.value()

    @value_changed
    def cursive_changed(self):
        self.draw.style.cursive = self.sCursive.value()

    @value_changed
    def thickness_changed(self):
        self.draw.style.thickness = self.sThickness.value()

    @value_changed
    def curl_changed(self):
        self.draw.style.curl = self.sCurl.value()

    @value_changed
    def xPos_changed(self):
        self.draw.style.xPos = self.sXPos.value()

    @value_changed
    def yPos_changed(self):
        self.draw.style.yPos = self.sYPos.value()

        #self.obj.style.color = self.sSize.value()