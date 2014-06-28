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

        current_language_button = QtGui.QPushButton('English')
        current_language_button.clicked.connect(self.switchLanguage)
        self.current_language_button = current_language_button

        check_button =  QtGui.QPushButton('Check')
        #check_button.clicked.connect(self.check)
        self.check_button = check_button

        word_box = QtGui.QTextEdit('')
        translation_box = QtGui.QTextEdit('')
        self.word_box = word_box
        self.translation_box = translation_box

        case_label = QtGui.QLabel('Cases:')
        all_cases_label = QtGui.QLabel('Nominativ, Akkusativ, Dativ, Genitiv')
        der_die_das_label = QtGui.QLabel('')
        self.der_die_das_label = der_die_das_label

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(back_button, 0, 0)
        grid.addWidget(current_language_button, 1, 0)
        grid.addWidget(check_button, 2, 0)
        grid.addWidget(word_box, 3, 0)
        grid.addWidget(translation_box, 3, 2)
        grid.addWidget(case_label, 0, 2)
        grid.addWidget(all_cases_label, 1, 2)
        grid.addWidget(der_die_das_label, 2, 2)

        self.setWindowTitle('Prufung Mode')
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