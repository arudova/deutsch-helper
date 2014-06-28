import sys
from main_application import MainScreen
from PySide import QtGui

def main():
    
    app = QtGui.QApplication(sys.argv)
    main_screenshowMode = MainScreen()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()