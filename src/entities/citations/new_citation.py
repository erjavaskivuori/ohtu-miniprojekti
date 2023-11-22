from citations.citation_type import CitationType

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
    def __init__(self, type: CitationType, attributeNames: list[str]):
        self.type = type
        self.attributes:list[CitationAttribute] = []
        for s in attributeNames:
            self.attributes.append(CitationAttribute(s))
    
    def __str__(self):
        returnString = ""
        for attribute in self.attributes:
            returnString += str(attribute) + "\n"
        return returnString