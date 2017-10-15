"""PBCore Creator - a GUI tool for creating and managing PBCore metadata

Requires python 3 and PyQT5

"""

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

    """Manages the setup and display of the main GUI window

    """

    def __init__(self, parent=None):
        """Start up and configure the main window

        Open window
        Create objects for the PBCore and Premis elements
        Set up signals and slots

        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.menuBar.setNativeMenuBar(False)

        buildMenu(config["language"], self.language_choice)

        ##### create element objects

        # The arguments are a list of options for dropdowns (except AnalogPremis), and the Qt widget
        # being handled by that object. 

        # The options list are eventually used by genericInputBox()
        # to create the appropriate elements in the QComboBox selector

        # The widget is used by the CRUD functions to know which GUI element to update

        self.titles = PBcoreTitle(config["title"], self.title_list)
        self.descriptions = PBcoreDescription(config["description"], self.description_list)
        self.dates = PBcoreDate(config["date"], self.date_list)
        self.coverages = PBcoreCoverage(config["coverage"], self.coverage_list)
        self.creators = PBcoreCreator(config["creator"], self.creator_list)
        self.contributors = PBcoreContributor(config["creator"], self.contributor_list)
        self.publishers = PBcorePublisher(config["publisher"], self.publisher_list)
        self.analogpremis = AnalogPremis(self.analogpremis_list)

        ##### set up signals/slots

        # TODO THESE NEED TO HAVE THEIR OWN SPECIAL DIALOGS: rights

        ## enable/disable "remove" buttons

        self.title_list.itemSelectionChanged.connect(lambda: self.removeButtonToggle(self.title_list, self.title_removebutton))
        self.description_list.itemSelectionChanged.connect(lambda: self.removeButtonToggle(self.description_list, self.description_removebutton))
        self.date_list.itemSelectionChanged.connect(lambda: self.removeButtonToggle(self.date_list, self.date_removebutton))
        self.coverage_list.itemSelectionChanged.connect(lambda: self.removeButtonToggle(self.coverage_list, self.coverage_removebutton))
        self.creator_list.itemSelectionChanged.connect(lambda: self.removeButtonToggle(self.creator_list, self.creator_removebutton))
        self.contributor_list.itemSelectionChanged.connect(lambda: self.removeButtonToggle(self.contributor_list, self.contributor_removebutton))
        self.publisher_list.itemSelectionChanged.connect(lambda: self.removeButtonToggle(self.publisher_list, self.publisher_removebutton))
        self.language_list.itemSelectionChanged.connect(lambda: self.removeButtonToggle(self.language_list, self.language_removebutton))
        self.rights_list.itemSelectionChanged.connect(lambda: self.removeButtonToggle(self.rights_list, self.rights_removebutton))
        self.analogpremis_list.itemSelectionChanged.connect(lambda: self.removeButtonToggle(self.analogpremis_list, self.analogpremis_removebutton))
        self.digitalinstantiation_list.itemSelectionChanged.connect(lambda: self.removeButtonToggle(self.digitalinstantiation_list, self.digitalinstantiation_removebutton))

        ## menu items

        self.actionExport.triggered.connect(self.export)

        ## GUI elements

        # "add" buttons

        self.title_addbutton.clicked.connect(lambda: self.genericInputbox(self.titles))
        self.description_addbutton.clicked.connect(lambda: self.genericInputbox(self.descriptions))
        self.date_addbutton.clicked.connect(lambda: self.genericInputbox(self.dates))
        self.coverage_addbutton.clicked.connect(lambda: self.genericInputbox(self.coverages))
        self.creator_addbutton.clicked.connect(lambda: self.genericInputbox(self.creators))
        self.contributor_addbutton.clicked.connect(lambda: self.genericInputbox(self.contributors))
        self.publisher_addbutton.clicked.connect(lambda: self.genericInputbox(self.publishers))
        #self.language_addbutton.clicked.connect()
        # TODO rights
        self.analogpremis_addbutton.clicked.connect(lambda: self.analogPremisInputbox(self.analogpremis))

        ## "remove" buttons
        self.title_removebutton.clicked.connect(lambda: self.removeElement(self.titles))
        self.description_removebutton.clicked.connect(lambda: self.removeElement(self.descriptions))
        self.date_removebutton.clicked.connect(lambda: self.removeElement(self.dates))
        self.coverage_removebutton.clicked.connect(lambda: self.removeElement(self.coverages))
        self.creator_removebutton.clicked.connect(lambda: self.removeElement(self.creators))
        self.contributor_removebutton.clicked.connect(lambda: self.removeElement(self.contributors))
        self.publisher_removebutton.clicked.connect(lambda: self.removeElement(self.publishers))
        # TODO language
        # TODO rights
        self.analogpremis_removebutton.clicked.connect(lambda: self.removeElement(self.analogpremis))
   
        # deal with double clicks on list boxes
        self.title_list.itemDoubleClicked.connect(lambda: self.editPBcoreElement(self.titles))
        self.description_list.itemDoubleClicked.connect(lambda: self.editPBcoreElement(self.descriptions))
        self.date_list.itemDoubleClicked.connect(lambda: self.editPBcoreElement(self.dates))
        self.coverage_list.itemDoubleClicked.connect(lambda: self.editPBcoreElement(self.coverages))
        self.creator_list.itemDoubleClicked.connect(lambda: self.editPBcoreElement(self.creators))
        self.contributor_list.itemDoubleClicked.connect(lambda: self.editPBcoreElement(self.contributors))
        self.publisher_list.itemDoubleClicked.connect(lambda: self.editPBcoreElement(self.publishers))
        #self.language_list.itemDoubleClicked.connect(lambda: self.editPBcoreElement(self.languag_list, self.language_removebutton))
        #self.rights_list.itemDoubleClicked.connect(lambda: self.editPBcoreElement(self.rights_list, self.rights_removebutton))


        ## populate analog instance menu
        
        buildMenu(config["instantiationPhysical"], self.analog_type)


    def export(self):
        """Function to handle export of PBCore and Premis XML for each element

        Makes use of the makeXML methods of each element object

        """
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
        """Display and configure a generic input Qt dialog and perform a create operation
        for list object element

        This dialog is used for nearly all PBCore elements, but not for Premis events.

        listobj: the element object corresponding to the desired input

        The function uses the values in listobj.options to construct the QComboBox dropdown using the
        buildMenu() function, and in response to an "ok" click creates a new PBcoreElement object
        containing the returned attribute and value. This object is then appended to the listobj and 
        added to the QListWidget stored in the list_element instance variable for the listobj.

        """
        dlg = StartGenericInputbox()
        buildMenu(listobj.options, dlg.attribute)

        if dlg.exec_():
            input = dlg.getValues()
            data = PBcoreElement(input["attribute"], input["attribute-index"], input["text"])
            listbox = listobj.list_element
            listbox.addItem(str(data))
            listobj.append(data)
        else:
            return

    def analogPremisInputbox(self, listobj):
        """Display and configure the Qt dialog for analog Premis events and perform a create operation
        for list object element

        Completely analogous to genericInputbox, except that there is an additional QComboBox dropdown
        and additional arguments for the Premis agent and event date.

        """
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
        """Toggle the enabled state of a "remove" button

        Enable "remove" button only if at least one item is selected in the corresponding QListWidget.

        listbox: the QListWidget
        button: the "remove" QToolButton the state of which should be toggled

        """
        if len(listbox.selectedItems()) > 0:
            button.setEnabled(True)
        else:
            button.setEnabled(False)

    def removeElement(self, listobj):
        """Perform a delete operation on a element list object

        Queries the current selected item in the QListWidget specified
        by the listobj argument, and deletes it from both the list object and the 
        QListWidget.

        """
        listbox = listobj.list_element
        current_item = listbox.currentItem()
        current_row = listbox.row(current_item)
        del listobj[current_row]
        listbox.takeItem(current_row)

    def editPBcoreElement(self, listobj):
        """Performs an update operation on an element list object

        Uses the same generic input box as for the create operation

        """
        listbox = listobj.list_element
        current_item = listbox.currentItem()
        current_row = listbox.row(current_item)

        dlg = StartGenericInputbox()
        buildMenu(listobj.options, dlg.attribute)

        # set dialog objects to current values
        dlg.text.document().setPlainText(listobj[current_row].text)
        dlg.attribute.setCurrentIndex(listobj[current_row].attribute_index)

        if dlg.exec_():
            input = dlg.getValues()
            data = PBcoreElement(input["attribute"], input["attribute-index"], input["text"])
            listobj[current_row] = data
            current_item.setText(str(data))
        else:
            return

def buildMenu(all_attributes, menu_object):
    """Utility function to process and insert element list into a QComboBox dropdown

    Processes settings from config file and builds element list for the dropdown.
    Detects "#" and "-" in the config data, terminates the menu at the first occurence of "#"
    and replaces "-" with separator elements.

    all_attributes: list containing the raw elements from the config file
    menu_object: the QComboBox widget to be configured

    """
    # deal with end delimiter
    attributes = [list(group) for k, group in groupby(all_attributes, lambda x: x == "#") if not k][0]

    # deal with separators
    attributes = [list(group) for k, group in groupby(attributes, lambda x: x == "-") if not k]
    attributes = attributes[::-1]

    this_list = attributes.pop()
    menu_object.addItems(this_list)

    while (len(attributes) > 0):
        menu_object.insertSeparator(menu_object.count())
        this_list = attributes.pop()
        menu_object.addItems(this_list)


class StartGenericInputbox(QtWidgets.QDialog, Ui_GenericInputbox):

    """Displays and gathers return valus for a generic input dialog

    """

    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)

    def getValues(self):
        return {"attribute": str(self.attribute.currentText()), 
                "attribute-index": self.attribute.currentIndex(),
                "text": self.text.toPlainText()}

class StartPremisInputbox(QtWidgets.QDialog, Ui_AnalogpremisInputbox):

    """Displays and gathers return valus for a Premis input dialog

    """
    
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

