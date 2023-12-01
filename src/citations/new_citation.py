from enum import Enum


class CitationType(Enum):
    BOOK = 1
    ARTICLE = 2
    INPROCEEDINGS = 3


class CitationAttribute:
    def __init__(self, name: str):
        self.name = name
        self.value = ""

    def get_value(self):
        return self.value

    def get_name(self):
        return self.name

    def set_value(self, value: str):
        self.value = value

    def __str__(self):
        return self.name + ": " + str(self.value)


class Citation():
    def __init__(self, citation_type: CitationType, attribute_names: list[str]):
        self.type = citation_type
        self.tag = ""
        self.label = "antakaa_minulle_nimi_:( )"
        self.attributes: list[CitationAttribute] = []
        for s in attribute_names:
            self.attributes.append(CitationAttribute(s))

    def __str__(self):
        return_string = ""
        for attribute in self.attributes:
            return_string += str(attribute) + "\n"
        return return_string

    def get_attributes_dictionary(self):
        adict = {}
        for attribute in self.attributes:
            adict[attribute.get_name()] = attribute.get_value()

        return adict
    
    def set_tag(self,tag):
        self.tag = tag
