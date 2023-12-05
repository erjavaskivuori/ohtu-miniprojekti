from citations.new_citation import Citation, CitationType
from citations.citation_factory import CitationFactory
from citations.bibtex_maker import BibTexMaker
from citations.citation_strings import ATTR_TRANSLATIONS
from db.citation_repository import citation_repository
from db.tag_repository import tag_repository
from tui.tui import Tui

# Näin että stringit aina mätsäävät eikä kirjoitusvirhe
# esimerkiksi failaa testejä
TIEDOSTON_LUONTI_EPAONNISTUI = "Tiedoston luonti epäonnistui \
(tarkista oikeudet tai käytitkö kiellettyjä merkkejä)"
TIEDOSTON_LUONTI_ONNISTUI = "Tiedosto luotu onnistuneesti"


class CitationManager():
    """Class responsible of the application logic.
    """

    def __init__(self, tui, citation_repo=citation_repository,
                 tag_repo=tag_repository):
        """Class constructor. Creates service responsible of the application logic.

        Args:
            tui: user interface as a Tui object
            citation_repo: Defaults to citation_repository.
            tag_repo: Defaults to tag_repository.
        """
        self._tui: Tui = tui
        self._citation_repo = citation_repo
        self._tag_repo = tag_repo

    def add_citation(self, citation: Citation):
        """Creates new citation.
        Args:
            citation: citation to be created as a Citation object.
        """
        citation_id = self._citation_repo.create_citation(citation)

        return citation_id

    def add_citation_by_user_input(self):
        """Creates new citation by user input.

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

        return citation_id

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

    def add_tag_for_citation_by_user_input(self):
        """Adds tag for a citation by user input.

        Returns:
            True
        """
        if self.return_all_citations() == {}:
            self._tui.print_error("sinulla ei ole vielä yhtään sitaattia")
            return False

        self._tui.print("Lista kaikista sitaateistasi:")
        self.print_all()
        citation_id = self._tui.ask(
            "sen sitaatin id, jolle haluat lisätä tägin")

        if not self.citation_exists(citation_id):
            self._tui.print_error("Antamaasi id:tä ei ole olemassa")
            citation_id = self._tui.ask(
            "sen sitaatin id, jolle haluat lisätä tägin")

        if self.get_all_tags() != {}:
            self._tui.print("Lista olemassa olevista tageistasi:")
            self.print_all_tags()
            tag = self._tui.ask("Syötä jokin yllä olevista tägeista tai uusi tägi")
        else:
            tag = self._tui.ask("uusi tägi")

        if not self.add_tag_for_citation(citation_id, tag.lower()):
            self._tui.print_error("sitaatilla on jo tägi")

        return True

    def citation_exists(self, citation_id):
        all_citations = self.return_all_citations()

        for citation in all_citations.items():
            if int(citation[0]) == int(citation_id):
                return True

        return False

    def add_tag_for_citation(self, citation_id, tag):
        """Creates tag for citation.

        Args:
            citation_id (int): citation's id
            tag (str): tag's name
        """
        return self._tag_repo.add_tag_to_citation(citation_id, tag)

    def get_all_tags(self):
        return self._tag_repo.get_all_tags()

    def print_all_tags(self):

        all_tags = self.get_all_tags()

        for i in all_tags:
            self._tui.print(i)

    def return_one_citation(self, title: str):
        """Method to get one citation from database.

        Args:
            title: title of a citation.

        Returns:
            Title of a citation. None if there isn't mathcing citations.
        """

        return self._citation_repo.get_one_citation(title)

    def return_all_citations(self):
        """Method to list all saved citations.

        Returns:
            Dictionary of all citations.
            Dictionary contains ("id", Citation object).
        """

        return self._citation_repo.get_all_citations()

    def print_citation(self, c_id, c):
        """Method to print citation.

        Args:
            c_id: id of the citation to be printed
            c: Citation object
        """

        attributes = c.get_attributes_dictionary()
        self._tui.print_item_entry(c_id, "label_tähän")
        self._tui.print_item_attribute("type", c.type.name)
        for key, value in attributes.items():
            self._tui.print_item_attribute(
                f"{ATTR_TRANSLATIONS[key]} ({key})", value
            )
        if c.tag != "":
            self._tui.print_item_attribute("tägi", c.tag)

    def print_all(self):
        """Method to print all the citations saved in database.

        Returns:
            True
        """
        citations = self._citation_repo.get_all_citations()
        if len(citations) < 1:
            self._tui.print("Ei sitaatteja.")
            return False
        for c_id, citation in citations.items():
            self.print_citation(c_id, citation)
        return True

    def print_by_tag(self):
        """Method to print all the citations with a tag.
        """
        tag = self._tui.ask("tägi")
        for c_id, citation in self._citation_repo.get_all_citations().items():
            if citation.tag == tag:
                self.print_citation(c_id, citation)

    def clear_all(self):
        """Clears all the databses.
        """

        self._citation_repo.clear_table()
        self._tag_repo.clear_tables()

    def create_bib_file(self):
        """Creates .bib file.

        Returns: 
            True if succeed, False if didn't succeed
        """
        filename = self._tui.ask("tiedoston nimi (.bib)")
        if BibTexMaker.try_generate_bible_text_file(
            self.return_all_citations(),
            filename
        ):
            self._tui.output(TIEDOSTON_LUONTI_ONNISTUI)
            return True
        self._tui.output(TIEDOSTON_LUONTI_EPAONNISTUI)
        return False


    def delete_citation(self):
        citation_id = self._tui.ask("sitaatin id")
        self._citation_repo.delete_citation(citation_id)
        self._tag_repo.delete_by_citation_id(citation_id)

#    def search_citation(self, citation):
#        None


# if __name__=="__main__":
#     testi = Citation("a","a","a",11)
#     print(testi)
