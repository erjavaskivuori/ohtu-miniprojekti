from src.entities import Citation

class CitationManager():
    def __init__(self, citation = Citation):
        self.citation = citation

    def add_citation(self, type, author, title, year):
        new_citation = self.citation(type, author, title, year)
        
        return new_citation
        

