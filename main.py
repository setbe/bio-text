from biotext import BioText, TextStyle

from PyQt5.QtWidgets import QApplication
from sys import argv

style = TextStyle(fontsize=100, xPos=99, yPos=50)

app = QApplication(argv)
win = BioText(style)

win.textEdit.setText('''UVWXYZ''')
win.open_image(path = 'test-image.png')
win.show()
app.exec_()