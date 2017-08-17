import sys
from xml.etree import ElementTree as ET
from PBCoreElements import *
from PyQt5 import QtCore, QtGui, QtWidgets
from mainwindow import Ui_MainWindow
from genericInputbox import Ui_GenericInputbox
from analogpremis import Ui_AnalogpremisInputbox
from itertools import groupby

config = None

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.menuBar.setNativeMenuBar(False)

        ###############
        ##### create element objects
        ###############

        self.titles = PBcoreTitle(config["title"], self.title_list)
        self.descriptions = PBcoreDescription(config["description"], self.description_list)
        self.dates = PBcoreDate(config["date"], self.date_list)
        self.coverages = PBcoreCoverage(config["coverage"], self.coverage_list)
        self.creators = PBcoreCreator(config["creator"], self.creator_list)
        self.contributors = PBcoreContributor(config["creator"], self.contributor_list)
        self.publishers = PBcorePublisher(config["publisher"], self.publisher_list)
        self.analogpremis = AnalogPremis(self.analogpremis_list)

        ###############
        ##### set up signals/slots
        ###############

        # THESE NEED TO HAVE THEIR OWN SPECIAL DIALOGS: language, rights

        ##### enable/disable "remove" buttons

        self.title_list.itemSelectionChanged.connect(lambda: self.removeButtonToggle(self.title_list, self.title_removebutton))
        self.description_list.itemSelectionChanged.connect(lambda: self.removeButtonToggle(self.description_list, self.description_removebutton))
        self.date_list.itemSelectionChanged.connect(lambda: self.removeButtonToggle(self.date_list, self.date_removebutton))
        self.coverage_list.itemSelectionChanged.connect(lambda: self.removeButtonToggle(self.coverage_list, self.coverage_removebutton))
        self.creator_list.itemSelectionChanged.connect(lambda: self.removeButtonToggle(self.creator_list, self.creator_removebutton))
        self.contributor_list.itemSelectionChanged.connect(lambda: self.removeButtonToggle(self.contributor_list, self.contributor_removebutton))
        self.publisher_list.itemSelectionChanged.connect(lambda: self.removeButtonToggle(self.publisher_list, self.publisher_removebutton))
        self.title_list.itemSelectionChanged.connect(lambda: self.removeButtonToggle(self.title_list, self.title_removebutton))
        self.language_list.itemSelectionChanged.connect(lambda: self.removeButtonToggle(self.languag_list, self.language_removebutton))
        self.rights_list.itemSelectionChanged.connect(lambda: self.removeButtonToggle(self.rights_list, self.rights_removebutton))
        self.analogpremis_list.itemSelectionChanged.connect(lambda: self.removeButtonToggle(self.analogpremis_list, self.analogpremis_removebutton))
        self.digitalinstantiation_list.itemSelectionChanged.connect(lambda: self.removeButtonToggle(self.digitalinstantiation_list, self.digitalinstantiation_removebutton))

        ##### menu items

        self.actionExport.triggered.connect(self.export)

        ##### GUI elements

        ## "add" buttons
        self.title_addbutton.clicked.connect(lambda: self.genericInputbox(self.titles))
        self.description_addbutton.clicked.connect(lambda: self.genericInputbox(self.descriptions))
        self.date_addbutton.clicked.connect(lambda: self.genericInputbox(self.dates))
        self.coverage_addbutton.clicked.connect(lambda: self.genericInputbox(self.coverages))
        self.creator_addbutton.clicked.connect(lambda: self.genericInputbox(self.creators))
        self.contributor_addbutton.clicked.connect(lambda: self.genericInputbox(self.contributors))
        self.publisher_addbutton.clicked.connect(lambda: self.genericInputbox(self.publishers))
        # language
        # rights
        self.analogpremis_addbutton.clicked.connect(lambda: self.analogPremisInputbox(self.analogpremis))

        ## "remove" buttons
        self.title_removebutton.clicked.connect(lambda: self.removeElement(self.titles))
        self.description_removebutton.clicked.connect(lambda: self.removeElement(self.descriptions))
        self.date_removebutton.clicked.connect(lambda: self.removeElement(self.dates))
        self.coverage_removebutton.clicked.connect(lambda: self.removeElement(self.coverages))
        self.creator_removebutton.clicked.connect(lambda: self.removeElement(self.creators))
        self.contributor_removebutton.clicked.connect(lambda: self.removeElement(self.contributors))
        self.publisher_removebutton.clicked.connect(lambda: self.removeElement(self.publishers))
        # language
        # rights
        self.analogpremis_removebutton.clicked.connect(lambda: self.removeElement(self.analogpremis))
   
        # deal with double clicks on list boxes
        # self.ui.tophit_list.itemDoubleClicked.connect(self.clickAssign)

        ## populate analog instance menu
        all_attributes = config["instantiationPhysical"]

        # deal with end delimiter
        attributes = [list(group) for k, group in groupby(all_attributes, lambda x: x == "#") if not k][0]

        # deal with separators
        attributes = [list(group) for k, group in groupby(attributes, lambda x: x == "-") if not k]
        attributes = attributes[::-1]

        this_list = attributes.pop()
        self.analog_type.addItems(this_list)

        while (len(attributes) > 0):
            self.analog_type.insertSeparator(self.analog_type.count())
            this_list = attributes.pop()
            self.analog_type.addItems(this_list)


    def export(self):
        root = ET.Element("pbcore:pbcoreDescriptionDocument")
        root.set("xmlns:pbcore", "http://www.pbcore.org/PBCore/PBCoreNamespace.html")
        root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        root.set("xmlns:premis", "http://www.loc.gov/standards/premis/v2")
        root.set("xsi:schemaLocation", "http://www.pbcore.org/PBCore/PBCoreNamespace.html http://pbcore.org/xsd/pbcore-2.0.xsd http://www.loc.gov/standards/premis/v2 http://www.loc.gov/standards/premis/v2/premis-v2-2.xsd")

        root.extend(self.titles.makeXML())
        root.extend(self.descriptions.makeXML())
        root.extend(self.dates.makeXML())
        root.extend(self.coverages.makeXML())
        root.extend(self.creators.makeXML())
        root.extend(self.contributors.makeXML())
        root.extend(self.publishers.makeXML())
        
        print(ET.tostring(root))

    def genericInputbox(self, listobj):
        dlg = StartGenericInputbox()

        all_attributes = listobj.options

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
            data = PBcoreElement(input["attribute"], input["text"])
            listbox = listobj.list_element
            listbox.addItem(str(data))
            listobj.append(data)
        else:
            return

    def analogPremisInputbox(self, listobj):
        dlg = StartPremisInputbox()

        dlg.analogevent_type.addItems(config["analogpremisevent"])
        dlg.analogevent_agent.addItems(config["agent"])

        if dlg.exec_():
            input = dlg.getValues()
            data = PremisEvent(input["type"], input["date"], input["details"], input["agent"])
            listbox = listobj.list_element
            listbox.addItem(str(data))
            listobj.append(data)
        else:
            return

    def removeButtonToggle(self, listbox, button):
        if len(listbox.selectedItems()) > 0:
            button.setEnabled(True)
        else:
            button.setEnabled(False)


    def removeElement(self, listobj):
        listbox = listobj.list_element
        current_item = listbox.currentItem()
        current_row = listbox.row(current_item)
        del listobj[current_row]
        listbox.takeItem(current_row)


class StartGenericInputbox(QtWidgets.QDialog, Ui_GenericInputbox):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)

    def getValues(self):
        return {"attribute": str(self.attribute.currentText()), "text": self.text.toPlainText()}

class StartPremisInputbox(QtWidgets.QDialog, Ui_AnalogpremisInputbox):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)

    def getValues(self):
        return {"type": str(self.analogevent_type.currentText()), 
                    "date": self.analogevent_date.text(),
                    "details": self.analogevent_details.toPlainText(),
                    "agent": self.analogevent_agent.currentText()}

if __name__ == "__main__":
    import json

    with open('config.json') as data_file:    
        config = json.load(data_file)

    app = QtWidgets.QApplication(sys.argv)
    form = MainWindow()
    form.show()

    sys.exit(app.exec_())

