import sys
from PySide import QtGui, QtCore
from custom_db import CustomDB

class Check(QtGui.QWidget):
    windowSignal = QtCore.Signal(object)

    def __init__(self):
    	super(Check, self).__init__()
    
        self.initData()
        self.initUI()
        
    def initData(self):
    	sql = CustomDB()
    	sql.open()
    	self.data = sql.getDictionary()
    	sql.close()

    def initUI(self):
    	back_button = QtGui.QPushButton('Back')
        back_button.clicked.connect(self.showHome)

    	current_language_button = QtGui.QPushButton('English')
    	current_language_button.clicked.connect(self.switchLanguage)
    	self.current_language_button = current_language_button

    	grid = QtGui.QGridLayout()
        grid.setSpacing(10)
        
        grid.addWidget(back_button, 0, 0)
        grid.addWidget(current_language_button, 1, 0)

        self.setWindowTitle('Check Mode')
        self.setLayout(grid)

    def showHome(self):
        self.windowSignal.emit(0)

    def switchLanguage(self):
    	button = self.current_language_button
    	text = button.text()

    	if(text == 'English'):
    		button.setText('Deutsch')
    	else:
    		button.setText('English')
    		