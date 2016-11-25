
class PBcoreElement(None):
    def __init__(self, attribute, text):
        self.attribute = attribute
        self.text = text
        self.display = "[{}] {}".format(attribute, text.replace('\n', ' ').replace('\r', ''))
        self.display = (self.display[:20] + '...') if len(self.display) > 20 else self.display

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

class PBcoreTitle(PBcoreElement):
    allobj = []
    def __init__(self, attribute, text):
        super().__init__(attribute, text)

    def makeXML():
        pass


"title": self.title_list,
            "description": self.description_list,
            "date": self.date_list,
            "creator": self.creator_list,
            "publisher": self.publisher_list,
            "contributor": self.contributor_list,
            "rights": self.rights_list



class PBcore_AnalogPremis(None):
    def __init__(self):
        pass

class PBCore_DigitalPremis(None):
    def __init__(self):
        pass


class PBcore_DigitalInst(None):
    def __init__(self):
        pass


# need translation table for language names

