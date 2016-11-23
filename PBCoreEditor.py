import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import mainwindow
from mainwindow import Ui_MainWindow
from genericInputbox import Ui_GenericInputbox

config = None

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.menuBar.setNativeMenuBar(False)

        ###############
        ##### set up signals/slots
        ###############

        ##### menu items

        # self.ui.actionWhat.triggered.connect(self.what)

        ##### GUI elements

        self.description_addbutton.clicked.connect(lambda: self.genericInputbox("description"))
        self.title_addbutton.clicked.connect(lambda: self.genericInputbox("title"))
        self.date_addbutton.clicked.connect(lambda: self.genericInputbox("date"))
        self.coverage_addbutton.clicked.connect(lambda: self.genericInputbox("coverage"))
        # self.ui.tophit_list.itemDoubleClicked.connect(self.clickAssign)

    def genericInputbox(self, type):
        from itertools import groupby

        dlg = StartGenericInputbox(type)

        all_attributes = config[type]["values"]

        # deal with end delimiter
        attributes = [list(group) for k, group in groupby(all_attributes, lambda x: x == "#") if not k][0]

        # deal with separators
        attributes = [list(group) for k, group in groupby(attributes, lambda x: x == "-") if not k]
        attributes = attributes[::-1]

        this_list = attributes.pop()
        dlg.attribute.addItems(this_list)

        while (len(attributes) > 0):
            dlg.attribute.insertSeparator(dlg.attribute.count())
            this_list = attributes.pop()
            dlg.attribute.addItems(this_list)

        # dlg.attribute.addItems(attributes[1])
        # dlg.attribute.addItems(attributes[0])

        # dlg.attribute.addItems(attributes)

        if ("presets" in config[type]):
            dlg.preset.addItems(config[type]["presets"])
        else:
            dlg.preset.setEnabled(False) # would be nicer if it just vanished...

        if dlg.exec_(): 
            input = dlg.getValues() 
            self.description_list.addItem("({}) {}".format(input["attribute"], input["text"]))
        else:
            return

class StartGenericInputbox(QtWidgets.QDialog, Ui_GenericInputbox):
    def __init__(self, type=None, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)

    def getValues(self):
        return {"attribute": str(self.attribute.currentText()), "text": self.text.toPlainText()}


if __name__ == "__main__":
    import json

    with open('config.json') as data_file:    
        config = json.load(data_file)

    app = QtWidgets.QApplication(sys.argv)
    form = MainWindow()
    form.show()

    sys.exit(app.exec_())

