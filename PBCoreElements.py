
class PBcoreElement:
    def __init__(self, attribute, text):
        self.attribute = attribute
        self.text = text
        self.display = "[{}] {}".format(attribute, text.replace('\n', ' ').replace('\r', ''))
        self.display = (self.display[:45] + '...') if len(self.display) > 45 else self.display

    def __str__(self):
        return self.display

class PBcoreTitle(PBcoreElement):
    allobj = []
    def __init__(self, attribute, text):
        super().__init__(attribute, text)

    def makeXML():
        pass

class PBcoreDescription(PBcoreElement):
    allobj = []
    def __init__(self, attribute, text):
        super().__init__(attribute, text)

    def makeXML():
        pass

class PBcoreDate(PBcoreElement):
    allobj = []
    def __init__(self, attribute, text):
        super().__init__(attribute, text)

    def makeXML():
        pass

class PBcoreCreator(PBcoreElement):
    allobj = []
    def __init__(self, attribute, text):
        super().__init__(attribute, text)

    def makeXML():
        pass

class PBcorePublisher(PBcoreElement):
    allobj = []
    def __init__(self, attribute, text):
        super().__init__(attribute, text)

    def makeXML():
        pass

class PBcoreContributor(PBcoreElement):
    allobj = []
    def __init__(self, attribute, text):
        super().__init__(attribute, text)

    def makeXML():
        pass

class PBcoreCoverage(PBcoreElement):
    allobj = []
    def __init__(self, attribute, text):
        super().__init__(attribute, text)

    def makeXML():
        pass

### language

### rights

class PBcore_AnalogPremis:
    def __init__(self):
        pass

class PBCore_DigitalPremis:
    def __init__(self):
        pass


class PBcore_DigitalInst:
    def __init__(self):
        pass

