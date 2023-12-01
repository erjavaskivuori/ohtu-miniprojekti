"""Tarjoaa pääsyn Citation ja CitationType luokkaan"""
from citations.new_citation import Citation, CitationType
from citations.citation_strings import *

class CitationFactory():
    """Luo käyttövalmiin Citation olion kun sille antaa CitationTypen.
    Citation olio sisältää kaikki vaaditut arvot CitationAttribute listalla
    riippuen siitä mikä CitationType annettiin.
    """
    @staticmethod
    def get_new_citation(citation_type: CitationType):
        """Palauttaa uuden Citation objectin jonka attribuutit vastaavat annettua tyyppiä.
        """
        # hopefully temporary "if else hell":
        match citation_type:
            case CitationType.BOOK:
                return Citation(citation_type, BOOK_STRINGS)
            case CitationType.ARTICLE:
                return Citation(citation_type, ARTICLE_STRINGS)
            case CitationType.INPROCEEDINGS:
                return Citation(citation_type, INPROCEEDINGS_STRINGS)
        # default to book for now
        return Citation(citation_type, BOOK_STRINGS)

# Biblatex documentation:
# http://mirrors.ctan.org/macros/latex/contrib/biblatex/doc/biblatex.pdf
# (Entry types, starting from page 9)
# Example, Book:
# Requiredfields: author,title,year/date
# Optional fields: editor,editora,editorb,editorc,translator,
#   annotator,commentator,introduction,foreword,afterword, subtitle,
#   titleaddon,maintitle,mainsubtitle,maintitleaddon, language,
#   origlanguage,volume,part,edition,volumes,series, number,note,publisher,
#   location,isbn,eid,chapter,pages, pagetotal,addendum,pubstate,doi,eprint,eprintclass,
#   eprinttype,url,urldate
