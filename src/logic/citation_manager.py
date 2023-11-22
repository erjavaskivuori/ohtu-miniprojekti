from entities.citation import Citation
from db.citation_repository import citation_repository


class CitationManager():
    """Socelluslogiikasta vastaava luokka.
    """

    def __init__(self, citation_repo=citation_repository):
        """Luokan konstruktori. Luo uuden sovelluslogiikasta vastaavan palvelun.
        """

        self._citation_repo = citation_repo

    def add_citation(self, citation: Citation):
        """Luo uuden sitaatin.

        Args:
            citation: lisättävä sitaatti Citation-oliona.
        """

        self._citation_repo.create_citation(citation)

    
    def return_one_citation(self, title: str):
        """Hakee yhden sitaatin.

        Args:
            title: sitaatin otsikko.

        Returns:
            Palauttaa sitaatin, joka vastaa hakua. None jos sitaattia ei löydy.
        """

        return self._citation_repo.get_one_citation(title)
    
    
    def return_all_citaions(self):
        """Listaa kaikki sitaatit.

        Returns:
            Palauttaa listan kaikista sitaateista.
        """

        return self._citation_repo.get_all_citations()

    def print_all(self):
        """Tulostaa kaikki sitaatit.
        """

        citations = self._citation_repo.get_all_citations()

        for citation in citations:
            print(citation)

    def clear_all(self):
        """Tyhjentää tietokannan.
        """

        self._citation_repo.clear_table()

#    def delete_citation(self, citation):
#        None

#    def search_citation(self, citation):
#        None

# if __name__=="__main__":
#     testi = Citation("a","a","a",11)
#     print(testi)
