from collections import UserList
from xml.etree import ElementTree as ET
from xml.dom import minidom

def prettify(elem):
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")


class PBcoreElement:

    """The base class for storing all PBCore element metadata.

    Objects of this class are used as elements of the PBcoreList class.
    The class provides for an attribute/text pair, and also stores a "display"
    version of the contents that is suitable for display in a QListWidget

    """

    def __init__(self, attribute, attribute_index, text):
        self.attribute = attribute
        self.attribute_index = attribute_index
        self.text = text
        self.display = "[{}] {}".format(attribute, text.replace('\n', ' ').replace('\r', ''))
        self.display = (self.display[:45] + '...') if len(self.display) > 45 else self.display

    def __str__(self):
        return self.display

class PremisEvent:

    """The base class for storing all Premis event metadata.

    Objects of this class are used as elements of the PremisList class.
    The class provides for storage of event type, date, agent, and details.
    It also stores a "display" version of the contents that is suitable for display 
    in a QListWidget.

    """

    def __init__(self, type, date, details, agent):
        self.type = type
        self.date = date
        self.details = details
        self.agent = agent
        self.display = "{}: {}".format(date, type)
        self.display = (self.display[:45] + '...') if len(self.display) > 45 else self.display

    def __str__(self):
        return self.display

class PBcoreList(UserList):

    """The base class for lists used to store (potentially) multi-valued PBCore element metadata

    """

    def __init__(self, options, list_element, initial_list=[]):
        super().__init__(initial_list)
        self.options = options
        self.list_element = list_element

    def __getitem__(self, i):
        return self.data[i]

class PremisList(UserList):

    """The base class for lists used to store (potentially) multi-valued Premis event metadata

    """

    def __init__(self, list_element, initial_list=[]):
        super().__init__(initial_list)
        self.list_element = list_element


class PBcoreTitle(PBcoreList):

    """Child class of PBcoreList used for storing PBCore <pbcoreTitle> elements

    Provides a method for generating XML encoding of elements
    """

    def __init__(self, options, list_element):
        super().__init__(options, list_element)

    def makeXML(self):
        out = []
        for a in self:
            a_xml = ET.Element("pbcore:pbcoreTitle")
            a_xml.set("titleType", a.attribute)
            a_xml.text = a.text
            out.append(a_xml)

        return(out)

class PBcoreDescription(PBcoreList):

    """Child class of PBcoreList used for storing PBCore <pbcoreDescription> elements

    Provides a method for generating XML encoding of elements
    """
    
    def __init__(self, options, list_element):
        super().__init__(options, list_element)

    def makeXML(self):
        out = []
        for a in self:
            a_xml = ET.Element("pbcore:pbcoreDescription")
            a_xml.set("descriptionType", a.attribute)
            a_xml.text = a.text
            out.append(a_xml)
            
        return(out)

class PBcoreDate(PBcoreList):

    """Child class of PBcoreList used for storing PBCore <pbcoreAssetDate> elements

    Provides a method for generating XML encoding of elements
    """
    
    def __init__(self, options, list_element):
        super().__init__(options, list_element)

    def makeXML(self):
        out = []
        for a in self:
            a_xml = ET.Element("pbcore:pbcoreAssetDate")
            a_xml.set("dateType", a.attribute)
            a_xml.text = a.text
            out.append(a_xml)
            
        return(out)

class PBcoreCreator(PBcoreList):

    """Child class of PBcoreList used for storing PBCore <pbcoreCreator> elements

    Provides a method for generating XML encoding of elements
    """
    
    def __init__(self, options, list_element):
        super().__init__(options, list_element)

    def makeXML(self):
        out = []
        for a in self:
            a_xml = ET.Element("pbcore:pbcoreCreator")
            creator = ET.SubElement(a_xml, "pbcore:creator")
            creator.text = a.text
            creatorrole = ET.SubElement(a_xml, "pbcore:creatorRole")
            creatorrole.text = a.attribute
            out.append(a_xml)
            
        return(out)

class PBcorePublisher(PBcoreList):

    """Child class of PBcoreList used for storing PBCore <pbcorePublisher> elements

    Provides a method for generating XML encoding of elements
    """
    
    def __init__(self, options, list_element):
        super().__init__(options, list_element)

    def makeXML(self):
        out = []
        for a in self:
            a_xml = ET.Element("pbcore:pbcorePublisher")
            creator = ET.SubElement(a_xml, "pbcore:publisher")
            creator.text = a.text
            creatorrole = ET.SubElement(a_xml, "pbcore:publisherRole")
            creatorrole.text = a.attribute
            out.append(a_xml)
            
        return(out)

class PBcoreContributor(PBcoreList):

    """Child class of PBcoreList used for storing PBCore <pbcoreContributor> elements

    Provides a method for generating XML encoding of elements
    """
    
    def __init__(self, options, list_element):
        super().__init__(options, list_element)

    def makeXML(self):
        out = []
        for a in self:
            a_xml = ET.Element("pbcore:pbcoreContributor")
            creator = ET.SubElement(a_xml, "pbcore:contributor")
            creator.text = a.text
            creatorrole = ET.SubElement(a_xml, "pbcore:contributorRole")
            creatorrole.text = a.attribute
            out.append(a_xml)
            
        return(out)

class PBcoreCoverage(PBcoreList):

    """Child class of PBcoreList used for storing PBCore <pbcoreCoverage> elements

    Provides a method for generating XML encoding of elements
    """
    
    def __init__(self, options, list_element):
        super().__init__(options, list_element)

    def makeXML(self):
        out = []
        for a in self:
            a_xml = ET.Element("pbcore:pbcoreCoverage")
            creator = ET.SubElement(a_xml, "pbcore:coverage")
            creator.text = a.text
            creatorrole = ET.SubElement(a_xml, "pbcore:coverageType")
            creatorrole.text = a.attribute
            out.append(a_xml)
            
        return(out)

class PBcoreLanguage:

    """Child class of PBcoreList used for storing PBCore <pbcoreLanguage> elements

    Provides a method for generating XML encoding of elements
    """
    
    pass

class PBcoreRights:

    """Child class of PBcoreList used for storing PBCore <pbcoreRights> elements

    Provides a method for generating XML encoding of elements
    """
    
    pass

class AnalogPremis(PremisList):

    """Child class of PremisList used for storing Premis events for analog objects

    Provides a method for generating XML encoding of elements
    """
    
    def __init__(self, list_element):
        super().__init__(list_element)

    def makeXML(self):
        pass

class DigitalPremis:

    """Child class of PremisList used for storing Premis events for digital objects

    Provides a method for generating XML encoding of elements
    """

    def __init__(self):
        pass


class PBcoreDigitalInst:

    """Class for storing metadata about PBCore digitial instatiations 

    Provides a method for generating XML encoding of elements
    """

    def __init__(self):
        pass
