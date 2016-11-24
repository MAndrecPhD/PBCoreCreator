class PBcoreElement(None):
    def __init__(self, attribute, text):
        self.attribute = attribute
        self.text = text
        self.display = "[{}] {}".format(attribute, text.replace('\n', ' ').replace('\r', ''))

class PBcoreDescription(PBcoreElement):
    def __init__(self, attribute, text):
        super().__init__(attribute, text)

class PBcore_Contributor(None):
    pass


class PBcore_AnalogPremis(None):
    pass


class PBcore_DigitalInst(None):
    pass