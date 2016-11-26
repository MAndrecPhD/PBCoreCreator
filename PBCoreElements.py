from collections import UserList
from xml.etree import ElementTree as ET
from xml.dom import minidom

def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")


class PBcoreElement:
    def __init__(self, attribute, text):
        self.attribute = attribute
        self.text = text
        self.display = "[{}] {}".format(attribute, text.replace('\n', ' ').replace('\r', ''))
        self.display = (self.display[:45] + '...') if len(self.display) > 45 else self.display

    def __str__(self):
        return self.display

class PBcoreList(UserList):
    def __init__(self, options, list_element, initial_list=[]):
        super().__init__(initial_list)
        self.options = options
        self.list_element = list_element

    def __getitem__(self, i):
        return self.data[i]

class PBcoreTitle(PBcoreList):
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
    def __init__(self, options, list_element):
        super().__init__(options, list_element)

    def makeXML(self):
        pass

class PBcoreContributor(PBcoreList):
    def __init__(self, options, list_element):
        super().__init__(options, list_element)

    def makeXML(self):
        pass

class PBcoreCoverage(PBcoreList):
    def __init__(self, options, list_element):
        super().__init__(options, list_element)

    def makeXML(self):
        pass

class PBcoreLanguage:
    pass

class PBcoreRights:
    pass

class PBcore_AnalogPremis:
    def __init__(self):
        pass

class PBCore_DigitalPremis:
    def __init__(self):
        pass


class PBcore_DigitalInst:
    def __init__(self):
        pass
