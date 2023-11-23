from entities.citation import Citation
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
        self.add_citation( Citation(
            self._tui.ask("tyyppi"),
            self._tui.ask("tekijä"),
            self._tui.ask("otsikko"),
            self._tui.ask("vuosi", Citation.year_validator)
        ) )
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

        for c in  self._citation_repo.get_all_citations():
            self._tui.print_item_entry( 0, c.title )
            self._tui.print_item_attribute( "tyyppi", c.type )
            self._tui.print_item_attribute( "tekijä", c.author )
            self._tui.print_item_attribute( "vuosi", c.year )

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
