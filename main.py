from biotext import BioText

from PyQt5.QtWidgets import QApplication
from sys import argv

app = QApplication(argv)
win = BioText('A')
win.show()
app.exec_()