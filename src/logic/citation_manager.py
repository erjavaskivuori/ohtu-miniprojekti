from citations.new_citation import Citation, CitationType
from citations.citation_factory import CitationFactory
from db.citation_repository import citation_repository


class CitationManager():
    """Socelluslogiikasta vastaava luokka.
    """

    def __init__(self, tui, citation_repo=citation_repository):
        """Luokan konstruktori. Luo uuden sovelluslogiikasta vastaavan palvelun.
        """
        self._tui = tui
        self._citation_repo = citation_repo

    def add_citation(self, citation: Citation):
        """Luo uuden sitaatin.

        Args:
            citation: lisättävä sitaatti Citation-oliona.
        """
        self._citation_repo.create_citation(citation)

    def add_citation_by_user_input(self):
        """Luo uuden sitaatin kysellen käyttäjältä.

        Args:
            -
            
        TODO:
            * Make it ask relevant data for the citation type
            * Handle error situation and return False            
        """

        citation_type = self._tui.ask( \
        'tyypin numero, vaihtoehtoja ovat Kirja (1), Artikkeli (2) ja Inproceedings (3)', \
        self.type_validator)

        citation = CitationFactory.get_new_citation(CitationType(int(citation_type)))

        for attribute in citation.attributes:
            attribute.set_value(self._tui.ask(attribute.name))

        self.add_citation(citation)

        return True

    @staticmethod
    def type_validator(citation_type):
        try:
            i = int(citation_type)
            if i < 1 or i > 3:
                return False
        except ValueError:
            return False
        return True

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
        
            Tämä tässä vain esimerkkinä. CitationFactory ja Atribuutit käyttöön
        """

        citations = self._citation_repo.get_all_citations()

        for key in citations:
            c = citations[key]
            attributes = c.get_attributes_dictionary()
            self._tui.print_item_entry(key, attributes['title'])
            self._tui.print_item_attribute("type", c.type.name)
            for attribute in attributes:
                self._tui.print_item_attribute(attribute, attributes[attribute])

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
