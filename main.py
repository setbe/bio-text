from biotext import BioText, TextStyle

from PyQt5.QtWidgets import QApplication
from sys import argv

style = TextStyle()
style.fontsize = 200
style.xPos = 32

app = QApplication(argv)
win = BioText(style)

win.textEdit.setText('A')
win.open_image(path = 'test-image.png')
#win.export(just_show = True)
win.show()
app.exec_()