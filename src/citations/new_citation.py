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
        return self.name + ": " + self.value


class Citation():
    def __init__(self, citation_type: CitationType, attribute_names: list[str]):
        self.type = citation_type
        self.attributes: list[CitationAttribute] = []
        for s in attribute_names:
            self.attributes.append(CitationAttribute(s))

    def __str__(self):
        return_string = ""
        for attribute in self.attributes:
            return_string += str(attribute) + "\n"
        return return_string
