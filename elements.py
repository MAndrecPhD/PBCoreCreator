class PBcoreElement(None):
    def __init__(self, attribute, text):
        self.attribute = attribute
        self.text = text
        self.display = "[{}] {}".format(attribute, text.replace('\n', ' ').replace('\r', ''))

# adapter class?

class PBcoreDescription(PBcoreElement):
    def __init__(self, attribute, text):
        super().__init__(attribute, text)

    # function to generate XML

class PBcore_Contributor(PBcoreElement):
    def __init__(self, attribute, text):
        super().__init__(attribute, text)



class PBcore_AnalogPremis(PBcoreElement):
    def __init__(self, attribute, text):
        super().__init__(attribute, text)



class PBcore_DigitalInst(PBcoreElement):
    def __init__(self, attribute, text):
        super().__init__(attribute, text)
