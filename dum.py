import sys

from PyQt5 import QtCore, QtGui, QtWidgets
import mainwindow

class MainWindow(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)

    form = MainWindow()
    form.show()

    sys.exit(app.exec_())