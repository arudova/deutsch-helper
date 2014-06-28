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

        translate_button =  QtGui.QPushButton('Translate')
        translate_button.clicked.connect(self.translate)
        self.translate_button = translate_button

        word_box = QtGui.QTextEdit('Enter a word to be translated')
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
        grid.addWidget(translate_button, 2, 0)
        grid.addWidget(word_box, 3, 0)
        grid.addWidget(translation_box, 3, 2)
        grid.addWidget(case_label, 0, 2)
        grid.addWidget(all_cases_label, 1, 2)
        grid.addWidget(der_die_das_label, 2, 2)

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

    def translate(self):
        button = self.translate_button
        word = self.word_box.toPlainText()

        if(self.current_language_button.text()
            == 'English'):
            translated_word = [entry['english'] for entry in self.data
            if entry['deutsch'] == word]
        else:
            translated_word = [entry['deutsch'] for entry in self.data
            if entry['english'] == word]
            cases = [(entry['nominativ'], entry['akkusativ'],
            entry['dativ'], entry['genitiv']) for entry in self.data
            if entry['english'] == word]
            self.der_die_das_label.setText('%s, %s, %s, %s' % cases[0])

        self.translation_box.setText(translated_word[0])

