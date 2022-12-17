from biotext import BioText, TextStyle, TextRandom

from PyQt5.QtWidgets import QApplication
from sys import argv

style = TextStyle(fontname="miquy", fontsize=100, xPos=99, yPos=50, curl=3)

app = QApplication(argv)
win = BioText(style)

win.textEdit.setText('''o''')
win.open_image(path = 'test-image.png')
win.show()
app.exec_()