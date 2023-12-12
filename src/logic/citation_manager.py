from citations.new_citation import CitationType
from citations.citation_factory import CitationFactory
from citations.bibtex_maker import BibTexMaker
from citations.citation_strings import ATTR_TRANSLATIONS
from db.citation_repository import citation_repository
from db.tag_repository import tag_repository


class CitationManager():
    """Class responsible of the application logic.
    """

    def __init__(self, citation_repo=citation_repository,
                 tag_repo=tag_repository):
        """Class constructor. Creates service responsible of the application logic.

        Args:
            tui: user interface as a Tui object
            citation_repo: Defaults to citation_repository.
            tag_repo: Defaults to tag_repository.
        """
        self._citation_repo = citation_repo
        self._tag_repo = tag_repo

    def get_attrs_by_citation_type(self, citation_type):
        """Returns list of attribute names needes for citation type
        """
        return [x.name for x in CitationFactory.get_new_citation(
            CitationType(int(citation_type))).attributes]

    def add_citation(self, citation_type, label, tag, attrs):
        """ Creates new citation
        """
        citation = CitationFactory.get_new_citation(CitationType(citation_type))
        citation.set_label(label)

        for name, value in attrs.items():
            for a in citation.attributes:
                if a.get_name() == name:
                    a.set_value(value)

        try:
            citation_id = self._citation_repo.create_citation(citation)

            if tag != "":
                citation.set_tag(tag)
                self._tag_repo.add_tag_to_citation(citation_id, tag.lower())

            return True
        except (RuntimeError, AttributeError):
            return False

    def is_label_in_use(self, label):
        """ Return true if label is already in use
        """
        return self._citation_repo.is_label_already_used(label)

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

    def tag_by_citation(self, citation_id):

        return self._tag_repo.tag_by_citation_id(citation_id)

    def get_all_tags(self):
        return self._tag_repo.get_all_tags()

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
        attrs = []
        attrs.append(("type", c.type.name))
        for key, value in c.get_attributes_dictionary().items():
            attrs.append((f"{ATTR_TRANSLATIONS[key]} ({key})", value))
        if c.tag != "":
            attrs.append(("tägi", c.tag))
        return ((c_id, c.label), attrs)

    def get_plist(self):
        """Get print list of all citations

        Returns:
            List of citations in tuples ready to print
        """
        plist = []
        citations = self._citation_repo.get_all_citations()
        for c_id, citation in citations.items():
            plist.append(self.plist_entry(c_id, citation))
        return plist

    def get_plist_by_tag(self, tag):
        """Get print list entries tagges with tag

        Returns:
            List of citations in tuples ready to print
        """
        plist = []
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
        return True  # What if drop fails?

    def create_bib_file(self, filename):
        """Creates .bib file.

        Returns: 
            True if succeed, False if didn't succeed
        """
        return BibTexMaker.try_generate_bible_text_file(
            self.return_all_citations(), filename)

    def delete_citation(self, citation_id):
        """Deletes citation from database. if list is empty or 
        citation_id is not found, returns False
        """

        if self.return_all_citations() is None or not self.citation_exists(citation_id):
            return False

        self._citation_repo.delete_citation(citation_id)
        self._tag_repo.delete_by_citation_id(citation_id)

        return True
