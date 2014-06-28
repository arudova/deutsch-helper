import sys
from random import choice
from custom_db import CustomDB
from PySide import QtGui, QtCore


class Exam(QtGui.QWidget):
    windowSignal = QtCore.Signal(object)

    def __init__(self):
        super(Exam, self).__init__()

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

        check_button = QtGui.QPushButton('Check')
        check_button.clicked.connect(self.check)
        self.check_button = check_button

        word_box = QtGui.QTextEdit(choice(list(map(lambda entry:
                                                entry["english"],
                                                self.data))))
        translation_box = QtGui.QTextEdit('')
        self.word_box = word_box
        self.translation_box = translation_box

        case_label = QtGui.QLabel('Cases:')
        all_cases_label = QtGui.QLabel('Nominativ, Akkusativ, Dativ, Genitiv')
        der_die_das_label = QtGui.QLabel('')
        self.der_die_das_label = der_die_das_label

        correctness_label = QtGui.QLabel('')
        self.correctness_label = correctness_label

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
        grid.addWidget(correctness_label, 4, 0)

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

    def check(self):
        button = self.check_button

        if(button.text() == 'Check'):
            button.setText('Next')
            if(self.current_language_button.text() == 'English'):
                word_to_check = self.word_box.toPlainText()
                self.word_box.setText(word_to_check)
                correct_word = [entry['deutsch'] for entry in self.data
                                if entry['english'] == word_to_check]
                input_word = self.translation_box.toPlainText()
                if(input_word == correct_word[0]):
                    self.correctness_label.setText('Correct!')
                else:
                    self.correctness_label.setText('Incorrect!')
                word_to_check = choice(list(map(lambda entry:
                                                entry["english"],
                                                self.data)))
            else:
                word_to_check = self.word_box.toPlainText()
                self.word_box.setText(word_to_check)
                correct_word = [entry['english'] for entry in self.data
                                if entry['deutsch'] == word_to_check]
                input_word = translation_box.text()
                if(input_word == correct_word[0]):
                    correctness_label.setText('Correct!')
                else:
                    correctness_label.setText('Incorrect!')
                word_to_check = choice(list(map(lambda entry:
                                                entry["deutsch"],
                                                self.data)))
        else:
            self.check_button.setText('Check')
            if(self.current_language_button.text() == 'English'):
                word_to_check = choice(list(map(lambda entry:
                                                entry["english"],
                                                self.data)))
                self.word_box.setText(word_to_check)
                self.translation_box.setText('')
                self.correctness_label.setText('')
            else:
                word_to_check = choice(list(map(lambda entry:
                                                entry["deutsch"],
                                                self.data)))
                self.word_box.setText(word_to_check)
                self.translation_box.setText('')
                self.correctness_label.setText('')
