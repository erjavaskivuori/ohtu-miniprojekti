from citations.new_citation import CitationType
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


    def get_attrs_by_ctype(self, ctype):
        """Returns list of attribute names needes for citation type
        """
        return [ x.name for x in CitationFactory.get_new_citation(
            CitationType(int(ctype)) ).attributes ]


    def add_citation(self, ctype, label, tag, attrs):
        """ Creates new citation
        """
        citation = CitationFactory.get_new_citation(CitationType(ctype))
        citation.set_label(label)

        print(attrs)
        for name, value in attrs.items():
            for a in citation.attributes:
                if a.get_name() == name:
                    a.set_value( value )

        citation_id = self._citation_repo.create_citation(citation)

        if tag != "":
            citation.set_tag(tag)
            self._tag_repo.add_tag_to_citation(citation_id, tag.lower())

        return True # Maybe something can go wrong with db or so??

#    def is_label_in_use(self, label):
#        """ Return true if label is already in use
#        """
#        return False # self._citation_repo.label_used(label) ??


    def add_tag_for_citation_by_user_input(self):
        """Adds tag for a citation by user input.

        Returns:
            True
        """
        if self.return_all_citations() == {}:
            self._tui.print_error("sinulla ei ole vielä yhtään sitaattia")
            return False

        self._tui.print("Lista kaikista sitaateistasi:")

        citation_id = self._tui.ask(
            "sen sitaatin id, jolle haluat lisätä tägin")

        if not self.citation_exists(citation_id):
            self._tui.print_error("Antamaasi id:tä ei ole olemassa")
            return False

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

    def plist_entry(self, c_id, c):
        """Generates tuples ready print from citation

        Args:
            c_id: id of the citation to be printed
            c: Citation object
            
        Returns:
            (id, label), attrs[(key,val),(key,val)...]
        """
        attrs=[]
        attrs.append( ("type", c.type.name) )
        for key, value in c.get_attributes_dictionary().items():
            attrs.append( (f"{ATTR_TRANSLATIONS[key]} ({key})", value) )
        if c.tag != "":
            attrs.append( ("tägi", c.tag) )
        return ( (c_id, c.label) ,attrs )

    def get_plist(self):
        """Get print list of all citations

        Returns:
            List of citations in tuples ready to print
        """
        plist=[]
        citations = self._citation_repo.get_all_citations()
        for c_id, citation in citations.items():
            plist.append(self.plist_entry(c_id, citation))
        return plist


    def get_plist_by_tag(self, tag):
        """Get print list entries tagges with tag

        Returns:
            List of citations in tuples ready to print
        """
        plist=[]
        citations = self._citation_repo.get_all_citations()
        for c_id, citation in citations.items():
            if citation.tag == tag:
                plist.append(self.plist_entry(c_id, citation))
        return plist


    def clear_all(self):
        """Clears all the databses.
        """

        self._citation_repo.clear_table()
        self._tag_repo.clear_tables()
        return True # What if drop fails?

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

        return True # Fail should be handled

#    def search_citation(self, citation):
#        None


# if __name__=="__main__":
#     testi = Citation("a","a","a",11)
#     print(testi)
