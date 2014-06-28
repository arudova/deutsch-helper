import sys
from PySide import QtGui, QtCore

class Exam(QtGui.QWidget):
    windowSignal = QtCore.Signal(object)
    
    def __init__(self):
    	super(Exam, self).__init__()
    
        self.initUI()

    def initUI(self):
        back_button = QtGui.QPushButton('Back')
        back_button.clicked.connect(self.showHome)

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(back_button, 0, 0, 1, 3)

        self.setWindowTitle('Prufung Mode')
        self.setLayout(grid)

    def showHome(self):
        self.windowSignal.emit(0)