# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bio-text.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1338, 679)
        MainWindow.setMinimumSize(QtCore.QSize(200, 100))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        MainWindow.setFont(font)
        MainWindow.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        MainWindow.setStyleSheet("QWidget {\n"
"    selection-background-color: #28272C;\n"
"    font-size: 13px;\n"
"    border: 0px;\n"
"}\n"
"\n"
"QMainWindow {\n"
"    background-color: #38373E;\n"
"    color: white ;\n"
"}\n"
"\n"
"QMenuBar {\n"
"    background-color:#28272C;\n"
"    color: white ;\n"
"}\n"
"\n"
"QTabWidget::pane, QTabWidget::tab-bar, QTabWidget, QTabWidget::tab { /* The tab widget frame */\n"
"    border: 0px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    color: #52515C;\n"
"    background: #27262B;\n"
"    border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    min-width: 8ex;\n"
"    padding: 3px 8px 3px 8px;\n"
"    margin-left: 3px;\n"
"    margin-bottom: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background: #484750;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    color: white ;\n"
"\n"
"}\n"
"\n"
"QTabBar::tab:pressed {\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-bottom: 3px; /* make non-selected tabs look smaller */\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover {\n"
"   color: #28272C;\n"
"}\n"
"\n"
"QScrollBar, QScrollArea {\n"
"    border: 0px;\n"
"    margin: 8px 0px;\n"
"    background-color: none;\n"
"}\n"
"\n"
"QScrollBar::sub-page:vertical, QScrollBar::add-page:vertical, \n"
"QScrollBar::sub-line:vertical, QScrollBar::add-line:vertical, QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background-color: none;\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"    border: 0px;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QScrollBar::handle:hover {\n"
"    backround-color: #474750;\n"
"}\n"
"\n"
"QSpinBox, QComboBox {\n"
"    color: #D7D6E1;\n"
"    background-color: #52515C;\n"
"    border: 0px;\n"
"    padding: 4px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    border: 0px;\n"
"    width: 0px;\n"
"    height: 0px\n"
"}\n"
"\n"
"QSpinBox::up-arrow, QSpinBox::down-arrow {\n"
"    color: #474750;\n"
"    width: 7px;\n"
"    height: 7px;\n"
"}\n"
"\n"
"QSpinBox:hover, QComboBox:hover {\n"
"    color: white;\n"
"}\n"
"QGroupBox {\n"
"    color: #52515C; \n"
"    border: 1px dashed #43424A;\n"
"}\n"
"\n"
"QDockWidget QLabel {\n"
"    color: #7C7B8B;\n"
"}\n"
"\n"
"QDockWidget QLabel:hover {\n"
"    color: #9998AC;\n"
"}\n"
"\n"
"QDockWidget {\n"
"    background-color: #28272C;\n"
"    color: lightgray;\n"
"    border: 1px solid lightgray;\n"
"}\n"
"\n"
"QDockWidget::title {\n"
"    background-color: #28272C;\n"
"    padding: 5px;\n"
"    text-align: center;\n"
"    margin-top: 5px;\n"
"}\n"
"\n"
"QDockWidget::float-button {\n"
"    color: gray;\n"
"    left: 20px;\n"
"    top: 8px;\n"
"    subcontrol-position: top center;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: white;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setStyleSheet("QFrame {\n"
"    background-color: #302F35;\n"
"    border-radius: 12px;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lImage = QtWidgets.QLabel(self.frame_2)
        self.lImage.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.lImage.setFont(font)
        self.lImage.setStyleSheet("QLabel {\n"
"    font-size: 24px;\n"
"    background-color: #28272C;\n"
"}")
        self.lImage.setTextFormat(QtCore.Qt.RichText)
        self.lImage.setAlignment(QtCore.Qt.AlignCenter)
        self.lImage.setObjectName("lImage")
        self.verticalLayout_5.addWidget(self.lImage)
        self.horizontalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1338, 23))
        self.menubar.setStyleSheet("QMenuBar::item:selected {\n"
"    background-color: #38373E;\n"
"}\n"
"\n"
"QMenu::item {\n"
"    background-color: #28272C;\n"
"    color: #D7D6E1;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    background-color: #38373E;\n"
"    color: white;\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    height: 2px;\n"
"    background: #28272C;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"    border-color:  #28272C;\n"
"}\n"
"\n"
"QMenu::indicator {\n"
"    width: 0px;\n"
"    height: 0px;\n"
"}")
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSave = QtWidgets.QMenu(self.menuFile)
        self.menuSave.setObjectName("menuSave")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.dockStyle = QtWidgets.QDockWidget(MainWindow)
        self.dockStyle.setMinimumSize(QtCore.QSize(400, 200))
        self.dockStyle.setMaximumSize(QtCore.QSize(600, 524287))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.dockStyle.setFont(font)
        self.dockStyle.setStyleSheet("background-color: #28272C;")
        self.dockStyle.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.dockStyle.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockStyle.setObjectName("dockStyle")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout.setContentsMargins(10, 2, 16, 8)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.dockWidgetContents)
        self.scrollArea.setStyleSheet("QScrollBar::handle {\n"
"    border: 0px;\n"
"    border-radius: 8px;\n"
"    background-color: #37373E;\n"
"}")
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 437, 600))
        self.scrollAreaWidgetContents_2.setMinimumSize(QtCore.QSize(350, 600))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.setContentsMargins(-1, 2, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox.setStyleSheet("QSpinBox {\n"
"    background-color: #474750;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: 1px solid #474750;\n"
"    background-color: #2E3244;\n"
"    border-bottom-right-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox {\n"
"    background-color: #474750;\n"
"}\n"
"\n"
"QListView {\n"
"    color: #F4F3FF;\n"
"    background-color: #61616E;\n"
"    border: 1px solid white;\n"
"    border-radius: 2px;\n"
"    selection-background-color: black;\n"
"}")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.gridLayout.setContentsMargins(16, 20, 32, 12)
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(8)
        self.gridLayout.setObjectName("gridLayout")
        self.sThickness = QtWidgets.QSpinBox(self.groupBox)
        self.sThickness.setMaximumSize(QtCore.QSize(60, 16777215))
        self.sThickness.setAlignment(QtCore.Qt.AlignCenter)
        self.sThickness.setMinimum(1)
        self.sThickness.setMaximum(32)
        self.sThickness.setSingleStep(1)
        self.sThickness.setProperty("value", 3)
        self.sThickness.setObjectName("sThickness")
        self.gridLayout.addWidget(self.sThickness, 2, 1, 1, 1)
        self.lColor = QtWidgets.QLabel(self.groupBox)
        self.lColor.setObjectName("lColor")
        self.gridLayout.addWidget(self.lColor, 4, 0, 1, 1)
        self.lSize = QtWidgets.QLabel(self.groupBox)
        self.lSize.setObjectName("lSize")
        self.gridLayout.addWidget(self.lSize, 0, 0, 1, 1)
        self.lCurl = QtWidgets.QLabel(self.groupBox)
        self.lCurl.setObjectName("lCurl")
        self.gridLayout.addWidget(self.lCurl, 3, 0, 1, 1)
        self.lCursive = QtWidgets.QLabel(self.groupBox)
        self.lCursive.setObjectName("lCursive")
        self.gridLayout.addWidget(self.lCursive, 1, 0, 1, 1)
        self.sCursive = QtWidgets.QSpinBox(self.groupBox)
        self.sCursive.setMaximumSize(QtCore.QSize(60, 16777215))
        self.sCursive.setAlignment(QtCore.Qt.AlignCenter)
        self.sCursive.setMinimum(-100)
        self.sCursive.setMaximum(100)
        self.sCursive.setSingleStep(5)
        self.sCursive.setProperty("value", 0)
        self.sCursive.setObjectName("sCursive")
        self.gridLayout.addWidget(self.sCursive, 1, 1, 1, 1)
        self.sCurl = QtWidgets.QSpinBox(self.groupBox)
        self.sCurl.setMaximumSize(QtCore.QSize(60, 16777215))
        self.sCurl.setAlignment(QtCore.Qt.AlignCenter)
        self.sCurl.setMinimum(0)
        self.sCurl.setMaximum(24)
        self.sCurl.setProperty("value", 5)
        self.sCurl.setObjectName("sCurl")
        self.gridLayout.addWidget(self.sCurl, 3, 1, 1, 1)
        self.lThickness = QtWidgets.QLabel(self.groupBox)
        self.lThickness.setObjectName("lThickness")
        self.gridLayout.addWidget(self.lThickness, 2, 0, 1, 1)
        self.sSize = QtWidgets.QSpinBox(self.groupBox)
        self.sSize.setMaximumSize(QtCore.QSize(60, 16777215))
        self.sSize.setStyleSheet("")
        self.sSize.setAlignment(QtCore.Qt.AlignCenter)
        self.sSize.setMinimum(6)
        self.sSize.setMaximum(200)
        self.sSize.setProperty("value", 24)
        self.sSize.setObjectName("sSize")
        self.gridLayout.addWidget(self.sSize, 0, 1, 1, 1)
        self.cColor = QtWidgets.QComboBox(self.groupBox)
        self.cColor.setMinimumSize(QtCore.QSize(100, 0))
        self.cColor.setEditable(True)
        self.cColor.setPlaceholderText("")
        self.cColor.setObjectName("cColor")
        self.cColor.addItem("")
        self.cColor.addItem("")
        self.cColor.addItem("")
        self.cColor.addItem("")
        self.gridLayout.addWidget(self.cColor, 4, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 3)
        self.gridLayout.setColumnStretch(1, 2)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_2.setStyleSheet("QSpinBox {\n"
"    background-color: #474750;\n"
"}")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout_2.setContentsMargins(16, 16, 16, 16)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.sSizeMax = QtWidgets.QSpinBox(self.groupBox_2)
        self.sSizeMax.setMaximumSize(QtCore.QSize(60, 16777215))
        self.sSizeMax.setAlignment(QtCore.Qt.AlignCenter)
        self.sSizeMax.setMinimum(-10)
        self.sSizeMax.setMaximum(10)
        self.sSizeMax.setObjectName("sSizeMax")
        self.gridLayout_2.addWidget(self.sSizeMax, 1, 2, 1, 1)
        self.sCursiveMax = QtWidgets.QSpinBox(self.groupBox_2)
        self.sCursiveMax.setMaximumSize(QtCore.QSize(60, 16777215))
        self.sCursiveMax.setAlignment(QtCore.Qt.AlignCenter)
        self.sCursiveMax.setMinimum(-10)
        self.sCursiveMax.setMaximum(10)
        self.sCursiveMax.setObjectName("sCursiveMax")
        self.gridLayout_2.addWidget(self.sCursiveMax, 2, 2, 1, 1)
        self.sCurlMin = QtWidgets.QSpinBox(self.groupBox_2)
        self.sCurlMin.setMaximumSize(QtCore.QSize(60, 16777215))
        self.sCurlMin.setAlignment(QtCore.Qt.AlignCenter)
        self.sCurlMin.setMinimum(-10)
        self.sCurlMin.setMaximum(10)
        self.sCurlMin.setObjectName("sCurlMin")
        self.gridLayout_2.addWidget(self.sCurlMin, 4, 1, 1, 1)
        self.lThicknessRandom = QtWidgets.QLabel(self.groupBox_2)
        self.lThicknessRandom.setObjectName("lThicknessRandom")
        self.gridLayout_2.addWidget(self.lThicknessRandom, 3, 0, 1, 1)
        self.lFromRandom = QtWidgets.QLabel(self.groupBox_2)
        self.lFromRandom.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lFromRandom.setAlignment(QtCore.Qt.AlignCenter)
        self.lFromRandom.setObjectName("lFromRandom")
        self.gridLayout_2.addWidget(self.lFromRandom, 0, 1, 1, 1)
        self.lCursiveRandom = QtWidgets.QLabel(self.groupBox_2)
        self.lCursiveRandom.setObjectName("lCursiveRandom")
        self.gridLayout_2.addWidget(self.lCursiveRandom, 2, 0, 1, 1)
        self.sThicknessMin = QtWidgets.QSpinBox(self.groupBox_2)
        self.sThicknessMin.setMaximumSize(QtCore.QSize(60, 16777215))
        self.sThicknessMin.setAlignment(QtCore.Qt.AlignCenter)
        self.sThicknessMin.setMinimum(-10)
        self.sThicknessMin.setMaximum(10)
        self.sThicknessMin.setObjectName("sThicknessMin")
        self.gridLayout_2.addWidget(self.sThicknessMin, 3, 1, 1, 1)
        self.lCurlRandom = QtWidgets.QLabel(self.groupBox_2)
        self.lCurlRandom.setObjectName("lCurlRandom")
        self.gridLayout_2.addWidget(self.lCurlRandom, 4, 0, 1, 1)
        self.lSizeRandom = QtWidgets.QLabel(self.groupBox_2)
        self.lSizeRandom.setObjectName("lSizeRandom")
        self.gridLayout_2.addWidget(self.lSizeRandom, 1, 0, 1, 1)
        self.sSizeMin = QtWidgets.QSpinBox(self.groupBox_2)
        self.sSizeMin.setMaximumSize(QtCore.QSize(60, 16777215))
        self.sSizeMin.setAlignment(QtCore.Qt.AlignCenter)
        self.sSizeMin.setMinimum(-10)
        self.sSizeMin.setMaximum(10)
        self.sSizeMin.setObjectName("sSizeMin")
        self.gridLayout_2.addWidget(self.sSizeMin, 1, 1, 1, 1)
        self.sCursiveMin = QtWidgets.QSpinBox(self.groupBox_2)
        self.sCursiveMin.setMaximumSize(QtCore.QSize(60, 16777215))
        self.sCursiveMin.setAlignment(QtCore.Qt.AlignCenter)
        self.sCursiveMin.setMinimum(-10)
        self.sCursiveMin.setMaximum(10)
        self.sCursiveMin.setObjectName("sCursiveMin")
        self.gridLayout_2.addWidget(self.sCursiveMin, 2, 1, 1, 1)
        self.sThicknessMax = QtWidgets.QSpinBox(self.groupBox_2)
        self.sThicknessMax.setMaximumSize(QtCore.QSize(60, 16777215))
        self.sThicknessMax.setAlignment(QtCore.Qt.AlignCenter)
        self.sThicknessMax.setMinimum(-10)
        self.sThicknessMax.setMaximum(10)
        self.sThicknessMax.setObjectName("sThicknessMax")
        self.gridLayout_2.addWidget(self.sThicknessMax, 3, 2, 1, 1)
        self.lToRandom = QtWidgets.QLabel(self.groupBox_2)
        self.lToRandom.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lToRandom.setAlignment(QtCore.Qt.AlignCenter)
        self.lToRandom.setObjectName("lToRandom")
        self.gridLayout_2.addWidget(self.lToRandom, 0, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)
        self.sCurlMax = QtWidgets.QSpinBox(self.groupBox_2)
        self.sCurlMax.setMaximumSize(QtCore.QSize(60, 16777215))
        self.sCurlMax.setAlignment(QtCore.Qt.AlignCenter)
        self.sCurlMax.setMinimum(-10)
        self.sCurlMax.setMaximum(10)
        self.sCurlMax.setObjectName("sCurlMax")
        self.gridLayout_2.addWidget(self.sCurlMax, 4, 2, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_3.setMinimumSize(QtCore.QSize(0, 100))
        self.groupBox_3.setStyleSheet("QSpinBox {\n"
"    background-color: #474750;\n"
"}")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.gridLayout_3.setContentsMargins(16, 16, 82, 16)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lDivide = QtWidgets.QLabel(self.groupBox_3)
        self.lDivide.setObjectName("lDivide")
        self.gridLayout_3.addWidget(self.lDivide, 0, 0, 1, 1)
        self.sDivide = QtWidgets.QSpinBox(self.groupBox_3)
        self.sDivide.setMinimumSize(QtCore.QSize(60, 0))
        self.sDivide.setMaximumSize(QtCore.QSize(60, 16777215))
        self.sDivide.setAlignment(QtCore.Qt.AlignCenter)
        self.sDivide.setObjectName("sDivide")
        self.gridLayout_3.addWidget(self.sDivide, 0, 1, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 3)
        self.gridLayout_3.setColumnStretch(1, 2)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout.addWidget(self.scrollArea)
        self.dockStyle.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockStyle)
        self.dockEdit = QtWidgets.QDockWidget(MainWindow)
        self.dockEdit.setMinimumSize(QtCore.QSize(151, 191))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.dockEdit.setFont(font)
        self.dockEdit.setStyleSheet("background-color: #28272C;")
        self.dockEdit.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.dockEdit.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
        self.dockEdit.setObjectName("dockEdit")
        self.dockWidgetContents_3 = QtWidgets.QWidget()
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.dockWidgetContents_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textEdit = QtWidgets.QTextEdit(self.dockWidgetContents_3)
        self.textEdit.setStyleSheet("QWidget {\n"
"    background-color: #302F35;\n"
"}\n"
"\n"
"QTextEdit {\n"
"    border: 0px;\n"
"}\n"
"\n"
"\n"
"QTextEdit {\n"
"    font-size: 12px;\n"
"    border-radius: 4px;\n"
"    color: white;\n"
"    border: 1px solid #35353B;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QScrollBar, QScrollArea {\n"
"    border: 0px;\n"
"    margin: 8px 0px;\n"
"    background-color: #38373E;\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"    border: 0px;\n"
"    border-radius: 8px;\n"
"    background-color: #28272C;\n"
"}\n"
"\n"
"QScrollBar::sub-page, QScrollBar::add-page, QScrollBar::up-arrow,QScrollBar::down-arrow {\n"
"    background-color: none;\n"
"}")
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_2.addWidget(self.textEdit)
        self.dockEdit.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockEdit)
        self.dockImage = QtWidgets.QDockWidget(MainWindow)
        self.dockImage.setMinimumSize(QtCore.QSize(400, 409))
        self.dockImage.setMaximumSize(QtCore.QSize(600, 524287))
        self.dockImage.setStyleSheet("background-color: #28272C;")
        self.dockImage.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.dockImage.setObjectName("dockImage")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setContentsMargins(10, 8, 32, 8)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_5 = QtWidgets.QGroupBox(self.dockWidgetContents_2)
        self.groupBox_5.setMinimumSize(QtCore.QSize(0, 100))
        self.groupBox_5.setStyleSheet("QSpinBox {\n"
"    background-color: #474750;\n"
"}\n"
"")
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_9.setContentsMargins(16, 16, 32, -1)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_7 = QtWidgets.QLabel(self.groupBox_5)
        self.label_7.setObjectName("label_7")
        self.gridLayout_9.addWidget(self.label_7, 0, 0, 1, 1)
        self.sXPos = QtWidgets.QSpinBox(self.groupBox_5)
        self.sXPos.setMinimumSize(QtCore.QSize(0, 0))
        self.sXPos.setMaximumSize(QtCore.QSize(60, 16777215))
        self.sXPos.setObjectName("sXPos")
        self.gridLayout_9.addWidget(self.sXPos, 0, 1, 1, 1)
        self.sYPos = QtWidgets.QSpinBox(self.groupBox_5)
        self.sYPos.setMinimumSize(QtCore.QSize(0, 0))
        self.sYPos.setMaximumSize(QtCore.QSize(60, 16777215))
        self.sYPos.setObjectName("sYPos")
        self.gridLayout_9.addWidget(self.sYPos, 0, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_5)
        self.label_8.setObjectName("label_8")
        self.gridLayout_9.addWidget(self.label_8, 1, 0, 1, 1)
        self.sWidth = QtWidgets.QSpinBox(self.groupBox_5)
        self.sWidth.setMinimumSize(QtCore.QSize(0, 0))
        self.sWidth.setMaximumSize(QtCore.QSize(60, 16777215))
        self.sWidth.setObjectName("sWidth")
        self.gridLayout_9.addWidget(self.sWidth, 1, 1, 1, 1)
        self.sHeight = QtWidgets.QSpinBox(self.groupBox_5)
        self.sHeight.setMinimumSize(QtCore.QSize(0, 0))
        self.sHeight.setMaximumSize(QtCore.QSize(60, 16777215))
        self.sHeight.setObjectName("sHeight")
        self.gridLayout_9.addWidget(self.sHeight, 1, 2, 1, 1)
        self.verticalLayout_4.addWidget(self.groupBox_5)
        self.groupBox_4 = QtWidgets.QGroupBox(self.dockWidgetContents_2)
        self.groupBox_4.setMinimumSize(QtCore.QSize(300, 0))
        self.groupBox_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_4.setStyleSheet("QSpinBox {\n"
"    background-color: #474750;\n"
"}\n"
"")
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_4.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.gridLayout_4.setContentsMargins(16, 16, 16, -1)
        self.gridLayout_4.setVerticalSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 9, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem1, 1, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem2, 1, 6, 1, 1)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.ax2 = QtWidgets.QSpinBox(self.groupBox_4)
        self.ax2.setMaximumSize(QtCore.QSize(46, 16777215))
        self.ax2.setMinimum(-9999)
        self.ax2.setMaximum(9999)
        self.ax2.setProperty("value", 0)
        self.ax2.setObjectName("ax2")
        self.gridLayout_8.addWidget(self.ax2, 1, 0, 1, 1)
        self.ay2 = QtWidgets.QSpinBox(self.groupBox_4)
        self.ay2.setMaximumSize(QtCore.QSize(46, 16777215))
        self.ay2.setMinimum(-9999)
        self.ay2.setMaximum(9999)
        self.ay2.setProperty("value", 0)
        self.ay2.setObjectName("ay2")
        self.gridLayout_8.addWidget(self.ay2, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_4)
        self.label_2.setMaximumSize(QtCore.QSize(46, 17))
        self.label_2.setText("X₂Y₂:")
        self.label_2.setObjectName("label_2")
        self.gridLayout_8.addWidget(self.label_2, 2, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_8, 4, 6, 1, 1)
        self.frame = QtWidgets.QFrame(self.groupBox_4)
        self.frame.setMinimumSize(QtCore.QSize(100, 100))
        self.frame.setMaximumSize(QtCore.QSize(100, 100))
        self.frame.setStyleSheet("background-color: #38373E;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_4.addWidget(self.frame, 6, 4, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 8, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem4, 6, 6, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem5, 4, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem6, 6, 2, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem7, 8, 7, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.ay3 = QtWidgets.QSpinBox(self.groupBox_4)
        self.ay3.setMaximumSize(QtCore.QSize(46, 16777215))
        self.ay3.setMinimum(-9999)
        self.ay3.setMaximum(9999)
        self.ay3.setProperty("value", 0)
        self.ay3.setObjectName("ay3")
        self.gridLayout_6.addWidget(self.ay3, 1, 1, 1, 1)
        self.ax3 = QtWidgets.QSpinBox(self.groupBox_4)
        self.ax3.setMaximumSize(QtCore.QSize(46, 16777215))
        self.ax3.setMinimum(-9999)
        self.ax3.setMaximum(9999)
        self.ax3.setProperty("value", 0)
        self.ax3.setObjectName("ax3")
        self.gridLayout_6.addWidget(self.ax3, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setMaximumSize(QtCore.QSize(46, 17))
        self.label_3.setText("X₃Y₃:")
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_6.addWidget(self.label_3, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_6, 8, 2, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem8, 9, 6, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label = QtWidgets.QLabel(self.groupBox_4)
        self.label.setMaximumSize(QtCore.QSize(46, 17))
        self.label.setText("X₁Y₁:")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 2, 1, 1, 1)
        self.ax1 = QtWidgets.QSpinBox(self.groupBox_4)
        self.ax1.setMaximumSize(QtCore.QSize(46, 16777215))
        self.ax1.setMinimum(-9999)
        self.ax1.setMaximum(9999)
        self.ax1.setProperty("value", 0)
        self.ax1.setObjectName("ax1")
        self.gridLayout_5.addWidget(self.ax1, 1, 0, 1, 1)
        self.ay1 = QtWidgets.QSpinBox(self.groupBox_4)
        self.ay1.setMaximumSize(QtCore.QSize(46, 16777215))
        self.ay1.setMinimum(-9999)
        self.ay1.setMaximum(9999)
        self.ay1.setProperty("value", 0)
        self.ay1.setObjectName("ay1")
        self.gridLayout_5.addWidget(self.ay1, 1, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_5, 4, 2, 1, 1)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.ay4 = QtWidgets.QSpinBox(self.groupBox_4)
        self.ay4.setMaximumSize(QtCore.QSize(46, 16777215))
        self.ay4.setMinimum(-9999)
        self.ay4.setMaximum(9999)
        self.ay4.setProperty("value", 0)
        self.ay4.setObjectName("ay4")
        self.gridLayout_7.addWidget(self.ay4, 1, 1, 1, 1)
        self.ax4 = QtWidgets.QSpinBox(self.groupBox_4)
        self.ax4.setMaximumSize(QtCore.QSize(46, 16777215))
        self.ax4.setMinimum(-9999)
        self.ax4.setMaximum(9999)
        self.ax4.setProperty("value", 0)
        self.ax4.setObjectName("ax4")
        self.gridLayout_7.addWidget(self.ax4, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setMaximumSize(QtCore.QSize(46, 17))
        self.label_4.setText("X₄Y₄:")
        self.label_4.setObjectName("label_4")
        self.gridLayout_7.addWidget(self.label_4, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_7, 8, 6, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem9, 4, 7, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setStyleSheet("font-size: 9px;")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 8, 4, 1, 1)
        self.verticalLayout_4.addWidget(self.groupBox_4)
        self.dockImage.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockImage)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setShortcut("Ctrl+O")
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setShortcut("Ctrl+E")
        self.actionExport.setObjectName("actionExport")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setShortcut("Ctrl+Q")
        self.actionQuit.setObjectName("actionQuit")
        self.actionStyle = QtWidgets.QAction(MainWindow)
        self.actionStyle.setShortcut("Ctrl+S")
        self.actionStyle.setObjectName("actionStyle")
        self.actionText = QtWidgets.QAction(MainWindow)
        self.actionText.setShortcut("Ctrl+T")
        self.actionText.setObjectName("actionText")
        self.menuSave.addAction(self.actionStyle)
        self.menuSave.addAction(self.actionText)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuSave.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BioText"))
        self.lImage.setText(_translate("MainWindow", "Open the image"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSave.setTitle(_translate("MainWindow", "Save"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuHelp.setTitle(_translate("MainWindow", "About"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.dockStyle.setWindowTitle(_translate("MainWindow", "Style"))
        self.groupBox.setTitle(_translate("MainWindow", "Font"))
        self.lColor.setText(_translate("MainWindow", "color:"))
        self.lSize.setText(_translate("MainWindow", "font-size:"))
        self.lCurl.setText(_translate("MainWindow", "curl:"))
        self.lCursive.setText(_translate("MainWindow", "cursive:"))
        self.lThickness.setText(_translate("MainWindow", "thickness:"))
        self.cColor.setCurrentText(_translate("MainWindow", "deep blue"))
        self.cColor.setItemText(0, _translate("MainWindow", "deep blue"))
        self.cColor.setItemText(1, _translate("MainWindow", "black"))
        self.cColor.setItemText(2, _translate("MainWindow", "blue"))
        self.cColor.setItemText(3, _translate("MainWindow", "red"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Random"))
        self.lThicknessRandom.setText(_translate("MainWindow", "thickness:"))
        self.lFromRandom.setText(_translate("MainWindow", "from"))
        self.lCursiveRandom.setText(_translate("MainWindow", "cursive:"))
        self.lCurlRandom.setText(_translate("MainWindow", "curl:"))
        self.lSizeRandom.setText(_translate("MainWindow", "font-size:"))
        self.lToRandom.setText(_translate("MainWindow", "to"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Misc"))
        self.lDivide.setText(_translate("MainWindow", "divide:"))
        self.dockEdit.setWindowTitle(_translate("MainWindow", "Edit"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "Your text here"))
        self.dockImage.setWindowTitle(_translate("MainWindow", "Text Overlay"))
        self.groupBox_5.setTitle(_translate("MainWindow", "General"))
        self.label_7.setText(_translate("MainWindow", "XY:"))
        self.label_8.setText(_translate("MainWindow", "Resolution:"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Anchors"))
        self.label_5.setText(_translate("MainWindow", "hold \"Shift\" to show"))
        self.actionOpen.setText(_translate("MainWindow", "Open image..."))
        self.actionSave_as.setText(_translate("MainWindow", "Save as..."))
        self.actionExport.setText(_translate("MainWindow", "Export..."))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionStyle.setText(_translate("MainWindow", "Style"))
        self.actionText.setText(_translate("MainWindow", "Text"))