import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import mainwindow
from mainwindow import Ui_MainWindow
from genericInputbox import Ui_GenericInputbox

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.menuBar.setNativeMenuBar(False)

        ###############
        ##### set up signals/slots
        ###############

        ##### menu items

        # self.ui.actionRun_matching.triggered.connect(self.runMatching)
        # self.ui.actionExport_CSV.triggered.connect(self.exportCSV)
        # self.ui.actionPreferences.triggered.connect(self.setPreferences)
        # self.ui.actionQuit.triggered.connect(QtCore.QCoreApplication.instance().quit)

        ##### GUI elements

        # self.desc_addbutton.clicked.connect(self.addDescription)
        # self.ui.tophit_list.itemDoubleClicked.connect(self.clickAssign)
        # self.ui.createAuthority_button.clicked.connect(self.createAuth)

#     def addDescription(self):
#         dlg = StartDescriptionDialog() 
#         if dlg.exec_(): 
#             match_method = dlg.getValues() 
#         else:
#             return

# class StartDescriptionDialog(QtWidgets.QDialog, Ui_DescriptionDialog):
#     def __init__(self, parent=None):
#         QtWidgets.QDialog.__init__(self, parent)
#         self.setupUi(self)

#     def getValues(self):
#         return 1


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    form = MainWindow()
    form.show()

    sys.exit(app.exec_())

