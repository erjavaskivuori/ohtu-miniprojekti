from citations.new_citation import Citation, CitationType
from citations.citation_factory import CitationFactory
from db.citation_repository import citation_repository
from db.tag_repository import tag_repository
from citations.bibtex_maker import BibTexMaker
from citations.citation_strings import ATTR_TRANSLATIONS


class CitationManager():
    """Socelluslogiikasta vastaava luokka.
    """

    def __init__(self, tui, citation_repo=citation_repository,
                 tag_repo=tag_repository):
        """Luokan konstruktori. Luo uuden sovelluslogiikasta vastaavan palvelun.
        """
        self._tui = tui
        self._citation_repo = citation_repo
        self._tag_repo = tag_repo

    def add_citation(self, citation: Citation):
        """Luo uuden sitaatin.
        Args:
            citation: lisättävä sitaatti Citation-oliona.
        """
        citation_id = self._citation_repo.create_citation(citation)

        return citation_id

    def add_citation_by_user_input(self):
        """Luo uuden sitaatin kysellen käyttäjältä.

        Args:
            -

        TODO:
            * Make it ask relevant data for the citation type
            * Handle error situation and return False            
        """

        citation_type = self._tui.ask(
            'tyypin numero, vaihtoehtoja ovat Kirja (1), Artikkeli (2) ja Inproceedings (3)',
            self.is_int_and_in_range_1_to_3_validator)
        if citation_type == "\0":
            return False

        citation = CitationFactory.get_new_citation(
            CitationType(int(citation_type)))

        for attribute in citation.attributes:
            if attribute.name == "year":
                attribute.set_value(self._tui.ask(
                    f"{ATTR_TRANSLATIONS[attribute.name]} ({attribute.name})",
                    self.year_validator
                ))
            else:
                attribute.set_value(self._tui.ask(
                    f"{ATTR_TRANSLATIONS[attribute.name]} ({attribute.name})"
                ))

        citation_id = self.add_citation(citation)

        if self._tui.yesno('Haluatko lisätä tägin'):
            tag = self._tui.ask('anna tägi')

            citation.set_tag(tag)

            self._tag_repo.add_tag_to_citation(citation_id, tag.lower())

        return True

    @staticmethod
    def year_validator(year):
        try:
            i = int(year)
            if i < 0 or i > 2040:
                return False
        except ValueError:
            return False
        return True

    @staticmethod
    def is_int_and_in_range_1_to_3_validator(citation_type):
        try:
            i = int(citation_type)
            if i < 1 or i > 3:
                return False
        except ValueError:
            return False
        return True

    def add_tag_for_citation(self):

        self._tui.print("Lista kaikista sitaateistasi:")
        self.print_all()
        citation_id = self._tui.ask(
            "sen sitaatin id, jolle haluat lisätä tägin")
        self._tui.print("Lista olemassa olevista tageistasi:")
        self.print_all_tags()
        tag = self._tui.ask("Syötä jokin yllä olevista tägeista tai uusi tägi")

        try:
            self._tag_repo.add_tag_to_citation(citation_id, tag.lower())
        except:
            self._tui.print_error("sitaatilla on jo tägi")

        return True

    def print_all_tags(self):

        all_tags = self._tag_repo.get_all_tags()

        for i in all_tags:
            self._tui.print(i)

    def return_one_citation(self, title: str):
        """Hakee yhden sitaatin.

        Args:
            title: sitaatin otsikko.

        Returns:
            Palauttaa sitaatin, joka vastaa hakua. None jos sitaattia ei löydy.
        """

        return self._citation_repo.get_one_citation(title)

    def return_all_citations(self):
        """Listaa kaikki sitaatit.

        Returns:
            Palauttaa dictionaryn kaikista sitaateista.
            Dictionary on muotoa ("id", Citation-olio).
        """

        return self._citation_repo.get_all_citations()

    def print_citation(self, c_id, c):
        attributes = c.get_attributes_dictionary()
        self._tui.print_item_entry(c_id, f"label_tähän")
        self._tui.print_item_attribute("type", c.type.name)
        for key, value in attributes.items():
            self._tui.print_item_attribute(
                f"{ATTR_TRANSLATIONS[key]} ({key})", value
            )
        if c.tag != "":
            self._tui.print_item_attribute("tägi", c.tag)

    def print_all(self):
        """Tulostaa kaikki sitaatit.
        """
        for c_id, citation in self._citation_repo.get_all_citations().items():
            self.print_citation(c_id, citation)

    def print_by_tag(self):
        """Tulostaa kaikki sitaatit jolla tagi.
        """
        tag = self._tui.ask("tägi")
        for c_id, citation in self._citation_repo.get_all_citations().items():
            if citation.tag == tag:
                self.print_citation(c_id, citation)

    def clear_all(self):
        """Tyhjentää tietokannan.
        """

        self._citation_repo.clear_table()

    def create_bib_file(self):
        filename = self._tui.ask("tiedoston nimi (.bib)")
        if BibTexMaker.try_generate_bible_text_file(
            self.return_all_citations(),
            filename
        ):
            self._tui.print("Tiedosto luotu onnistuneesti")
        else:
            self._tui.print_error("Tiedoston luonti epäonnistui")


#    def delete_citation(self, citation):
#        None

#    def search_citation(self, citation):
#        None


# if __name__=="__main__":
#     testi = Citation("a","a","a",11)
#     print(testi)
