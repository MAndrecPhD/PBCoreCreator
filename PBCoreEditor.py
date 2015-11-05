import sys
from PyQt4 import QtCore, QtGui
from mainwindow import Ui_MainWindow
from description import Ui_DescriptionDialog


class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ###############
        ##### set up signals/slots
        ###############

        ##### menu items

        # self.ui.actionRun_matching.triggered.connect(self.runMatching)
        # self.ui.actionExport_CSV.triggered.connect(self.exportCSV)
        # self.ui.actionPreferences.triggered.connect(self.setPreferences)
        # self.ui.actionQuit.triggered.connect(QtCore.QCoreApplication.instance().quit)

        ##### GUI elements

        self.ui.descriptionlist_plusbutton.clicked.connect(self.addDescription)
        # self.ui.tophit_list.itemDoubleClicked.connect(self.clickAssign)
        # self.ui.createAuthority_button.clicked.connect(self.createAuth)

    def addDescription(self):
        dlg = StartDescriptionDialog() 
        if dlg.exec_(): 
            match_method = dlg.getValues() 
        else:
            return

class StartDescriptionDialog(QtGui.QDialog, Ui_DescriptionDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)

    def getValues(self):
        return 1


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())

