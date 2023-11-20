from repositories.citation_repository import CitationRepository

class CitationManager():
    def __init__(self, citation_repo=CitationRepository):
        self._citation_repo = citation_repo

    def add_citation(self, type, author, title, year):
        new_citation = self._citation_repo.create_citation(type, author, title, year)
        

    def get_all_citations(self):
        citations = self._citation_repo.get_all_citations()
        return citations