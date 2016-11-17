import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from mainwindow import Ui_MainWindow
from description import Ui_DescriptionDialog


class StartQT5(Ui_MainWindow):
    def __init__(self, dialog):
        Ui_MainWindow.__init__(self)
        # self.ui = Ui_MainWindow()
        # self.ui.setupUi(self)

        ###############
        ##### set up signals/slots
        ###############

        ##### menu items

        # self.ui.actionRun_matching.triggered.connect(self.runMatching)
        # self.ui.actionExport_CSV.triggered.connect(self.exportCSV)
        # self.ui.actionPreferences.triggered.connect(self.setPreferences)
        # self.ui.actionQuit.triggered.connect(QtCore.QCoreApplication.instance().quit)

        ##### GUI elements

        # self.ui.descriptionlist_plusbutton.clicked.connect(self.addDescription)
        # self.ui.tophit_list.itemDoubleClicked.connect(self.clickAssign)
        # self.ui.createAuthority_button.clicked.connect(self.createAuth)

    def addDescription(self):
        dlg = StartDescriptionDialog() 
        if dlg.exec_(): 
            match_method = dlg.getValues() 
        else:
            return

# class StartDescriptionDialog(QtGui.QDialog, Ui_DescriptionDialog):
#     def __init__(self, parent=None):
#         QtGui.QDialog.__init__(self, parent)
#         self.setupUi(self)

#     def getValues(self):
#         return 1


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()

    prog = StartQT5(dialog)

    dialog.show()
    sys.exit(app.exec_())

