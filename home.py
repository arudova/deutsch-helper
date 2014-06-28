import sys
from PySide import QtGui, QtCore

class Home(QtGui.QWidget):
    windowSignal = QtCore.Signal(object)
    
    def __init__(self):
        super(Home, self).__init__()
        self.initUI()
        
    def initUI(self):
        prufung_button = QtGui.QPushButton('Prufung Mode')
        check_button = QtGui.QPushButton('Check Mode')

        prufung_button.clicked.connect(self.showPrufung)
        check_button.clicked.connect(self.showCheck)

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(prufung_button, 0, 0)
        grid.addWidget(check_button, 0, 1)

        self.setLayout(grid)
        self.setWindowTitle('Deutsch Helper')

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def showPrufung(self):
        self.windowSignal.emit(1)

    def showCheck(self):
        self.windowSignal.emit(2)


