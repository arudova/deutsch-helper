import sys
from PySide import QtGui, QtCore
from home import Home
from exam import Exam
from check import Check

class MainScreen(QtGui.QMainWindow):
    
    def __init__(self):
        super(MainScreen, self).__init__()

        self.initUI()
        self.initPages()

    def initUI(self):
        self.window_left = 0
        self.window_top = 0
        self.window_width = 800
        self.window_height = 600

        self.setWindowTitle('Deutsch Helper')
        self.setGeometry(self.window_left, self.window_top, self.window_width, self.window_height)
        self.center()
        self.show()

    def initPages(self):
        stackedWidget = QtGui.QStackedWidget()

        homeWidget = Home()
        examWidget = Exam()
        checkWidget = Check()
        homeWidget.windowSignal.connect(self.showMode)
        examWidget.windowSignal.connect(self.showMode)
        checkWidget.windowSignal.connect(self.showMode)

        pages = []
        pages.append(homeWidget)
        pages.append(examWidget)
        pages.append(checkWidget)

        for page in pages:
            stackedWidget.addWidget(page)

        self.stackedWidget = stackedWidget
        self.setCentralWidget(self.stackedWidget)

    def showMode(self, index):
        windowTitle = self.stackedWidget.widget(index).windowTitle()

        self.setWindowTitle(windowTitle)
        self.stackedWidget.setCurrentIndex(index)

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()