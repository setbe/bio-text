from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap
import PyQt5.QtCore as QtCore
from PyQt5.QtCore import QBuffer
from window import Ui_MainWindow

from PIL import Image
from PIL.ImageQt import ImageQt
import functools
import io

from textdraw import TextDraw
from style import TextStyle, TextRandom

class BioText(Ui_MainWindow, QMainWindow):
    def __init__(self, text_style: TextStyle = None):
        super(Ui_MainWindow, self).__init__()
        self.ui = self.setupUi(self)
        self.source = None
        self.draw = TextDraw(text_style)                 # TextDraw Class   // text render class
        self.image_fullsize = True
        
        self.connect_signals(text_style)

    def redraw_overlay(self):
        if self.source:
            if self.textEdit.toPlainText():
                y_margin = 0
                source = self.source.copy()
                for string in self.textEdit.toPlainText().split('\n'):
                    overlay = self.draw.draw(string, self.sDivide.value())
                    source.paste(overlay, (self.sXPos.value(), self.sYPos.value() + y_margin), overlay)
                    y_margin += self.draw.style.fontsize
                source = ImageQt(source)

                pixmap = QPixmap.fromImage(source)
                if not self.image_fullsize:
                    pixmap = pixmap.scaled(self.frame_2.width() - 20, self.frame_2.height() - 30, QtCore.Qt.KeepAspectRatio)
                self.lImage.setPixmap(pixmap)

    def open_image(self, event = None, path = None):
        if not self.source:
            if not path:
                imagePath, _ = QFileDialog.getOpenFileName()
            else:
                imagePath = path
            if imagePath:
                source_image = QPixmap(imagePath)
                if not source_image.isNull():
                    self.actionFullsize_Image.setEnabled(True)
                    self.source = QPixmap.toImage(source_image)
                    buffer = QBuffer()
                    buffer.open(QBuffer.ReadWrite)
                    self.source.save(buffer, 'PNG')
                    self.source = Image.open(io.BytesIO(buffer.data()))
                    if self.draw.style.fontsize == 0:
                        self.draw.style.fontsize = self.source.height // 20
                        self.sSize.setValue(self.draw.style.fontsize)
                    self.resize_source_image()
        else:
            self.image_fullsize = not self.image_fullsize
            self.resize_source_image()
    
    def resize_source_image(self, event = None):
        if self.source:
            self.redraw_overlay()

    def export(self):
        if self.source and self.textEdit.toPlainText():
            imagePath, _ = QFileDialog.getSaveFileName(self,"Export to...","","png;;jpg;;gif;;bpm;;jpeg;;webp")

            if imagePath:
                y_margin = 0
                source = self.source.copy()
                for string in self.textEdit.toPlainText().split('\n'):
                    overlay = self.draw.draw(string, self.sDivide.value(), is_export=True)
                    source.paste(overlay, (self.sXPos.value(), self.sYPos.value() + y_margin), overlay)
                    y_margin += self.draw.style.fontsize

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

    @value_changed
    def random_fontsize_changed(self):
        self.draw.style.random.fontsize = [self.sSizeMin.value(), self.sSizeMax.value()]

    @value_changed
    def random_cursive_changed(self):
        self.draw.style.random.cursive = [self.sCursiveMin.value(), self.sCursiveMax.value()]

    @value_changed
    def random_thickness_changed(self):
        self.draw.style.random.thickness = [self.sThicknessMin.value(), self.sThicknessMax.value()]

    @value_changed
    def random_curl_changed(self):
        self.draw.style.random.curl = [self.sCurlMin.value(), self.sCurlMax.value()]

    def connect_signals(self, text_style):
        if text_style:
            self.sSize.setValue(text_style.fontsize)
            self.sCursive.setValue(text_style.cursive)
            self.sThickness.setValue(text_style.thickness)
            self.sCurl.setValue(text_style.curl)

            self.sXPos.setValue(text_style.xPos)
            self.sYPos.setValue(text_style.yPos)

            self.sSizeMin.setValue(text_style.random.fontsize[0])
            self.sSizeMax.setValue(text_style.random.fontsize[1])

            self.sCursiveMin.setValue(text_style.random.cursive[0])
            self.sCursiveMax.setValue(text_style.random.cursive[1])

            self.sThicknessMin.setValue(text_style.random.thickness[0])
            self.sThicknessMax.setValue(text_style.random.thickness[1])

            self.sCurlMin.setValue(text_style.random.curl[0])
            self.sCurlMax.setValue(text_style.random.curl[1])

        # connections / signals
        self.textEdit.textChanged.connect(self.text_changed)

        self.lImage.mousePressEvent = self.open_image
        self.lImage.resizeEvent = self.resize_source_image
        # actions
        self.actionExport.triggered.connect(self.export)
        self.actionQuit.triggered.connect(self.quit)
        self.actionText.triggered.connect(self.save_text)
        self.actionFullsize_Image.triggered.connect(self.open_image)

        # spinboxes -- Style
        self.sSize.valueChanged.connect(self.fontsize_changed)
        self.sCursive.valueChanged.connect(self.spinbox_changed)
        self.sThickness.valueChanged.connect(self.thickness_changed)
        self.sCurl.valueChanged.connect(self.curl_changed)

        self.sSizeMin.valueChanged.connect(self.random_fontsize_changed)
        self.sSizeMax.valueChanged.connect(self.random_fontsize_changed)
        self.sCursiveMin.valueChanged.connect(self.random_cursive_changed)
        self.sCursiveMax.valueChanged.connect(self.random_cursive_changed)
        self.sThicknessMin.valueChanged.connect(self.random_thickness_changed)
        self.sThicknessMax.valueChanged.connect(self.random_thickness_changed)
        self.sCurlMin.valueChanged.connect(self.random_curl_changed)
        self.sCurlMax.valueChanged.connect(self.random_curl_changed)
        self.sDivide.valueChanged.connect(self.spinbox_changed)
        
        # spinboxes -- Text
        self.sXPos.valueChanged.connect(self.xPos_changed)
        self.sYPos.valueChanged.connect(self.yPos_changed)
        self.sWidth.valueChanged.connect(self.spinbox_changed)
        self.sHeight.valueChanged.connect(self.spinbox_changed)
        self.ax1.valueChanged.connect(self.spinbox_changed)