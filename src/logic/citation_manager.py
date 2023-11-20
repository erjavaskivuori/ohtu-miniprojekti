from entities.citation import Citation


class CitationManager():
    """Socelluslogiikasta vastaava luokka.
    """
    
    def __init__(self):
        """Luokan konstruktori. Luo uuden sovelluslogiikasta vastaavan palvelun.
        """

        self.all = []

    def add_citation(self, citation: Citation):
        """Luo uuden sitaatin.

        Args:
            citation: lisättävä sitaatti Citation-oliona.
        """

        self.all.append(citation)

    def return_all_citaions(self):
        """Listaa kaikki sitaatit.

        Returns:
            Palauttaa listan kaikista sitaateista.
        """

        return self.all

    def print_all(self):
        """Tulostaa kaikki sitaatit.
        """

        for citation in self.all:
            print(citation)

    def delete_citation(self, citation):
        None

    def search_citation(self, citation):
        None

# if __name__=="__main__":
#     testi = Citation("a","a","a",11)
#     print(testi)
