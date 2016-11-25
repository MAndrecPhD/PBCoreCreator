class PBcoreElement(None):
    def __init__(self, attribute, text):
        self.attribute = attribute
        self.text = text
        self.display = "[{}] {}".format(attribute, text.replace('\n', ' ').replace('\r', ''))

    # custom print method


# OR just make a GenericPBcoreElement with an argument indicating what it is:
#       class GenericPBcoreElement(None):
#           def __init__(self, type, attribute, text)
#
# and use it for everything except language and rights

class PBcoreDescription(PBcoreElement):
    def __init__(self, attribute, text):
        super().__init__(attribute, text)

    def makeXML():
        pass

class PBcore_Contributor(PBcoreElement):
    def __init__(self, attribute, text):
        super().__init__(attribute, text)



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

