import sys
from PBCoreElements import *
from PyQt5 import QtCore, QtGui, QtWidgets
from mainwindow import Ui_MainWindow
from genericInputbox import Ui_GenericInputbox

config = None

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.menuBar.setNativeMenuBar(False)

        self.widget_adapter = {  # MOVE THESE TO SIGNAL/SLOT SETUP
            "title": self.title_list,
            "description": self.description_list,
            "date": self.date_list,
            "creator": self.creator_list,
            "publisher": self.publisher_list,
            "contributor": self.contributor_list,
            "rights": self.rights_list
        }

        ###############
        ##### set up signals/slots
        ###############

        ##### menu items

        # self.ui.actionWhat.triggered.connect(self.what)

        ##### GUI elements

        ## "add" buttons
        self.description_addbutton.clicked.connect(
            lambda: self.genericInputbox("description", self.description_list, PBcoreDescription))
        self.title_addbutton.clicked.connect(
            lambda: self.genericInputbox("title", self.title_list, PBcoreTitle))
        self.date_addbutton.clicked.connect(
            lambda: self.genericInputbox("date", self.date_list, PBcoreDate))
        self.coverage_addbutton.clicked.connect(
            lambda: self.genericInputbox("coverage", self.coverage_list, PBcoreCoverage))
        self.creator_addbutton.clicked.connect(
            lambda: self.genericInputbox("creator", self.creator_list, PBcoreCreator))
        self.contributor_addbutton.clicked.connect(
            lambda: self.genericInputbox("creator", self.contributor_list, PBcoreContributor))
        self.publisher_addbutton.clicked.connect(
            lambda: self.genericInputbox("publisher", self.publisher_list, PBcorePublisher))

        # THESE NEED TO HAVE THEIR OWN SPECIAL DIALOGS
        # language
        # rights


        ## "remove" buttons
        ### ????
   
        ## forget about the up/down arrows for now (maybe forever)

        # deal with double clicks on list boxes
        # self.ui.tophit_list.itemDoubleClicked.connect(self.clickAssign)

    def genericInputbox(self, type, listbox, dataclass):
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

        if dlg.exec_():
            input = dlg.getValues()
            data = dataclass(input["attribute"], input["text"])
            listbox.addItem(str(data))
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

