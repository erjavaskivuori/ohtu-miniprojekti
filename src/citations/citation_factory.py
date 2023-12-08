from citations.new_citation import Citation, CitationType
from citations.citation_strings import ARTICLE_STRINGS, INPROCEEDINGS_STRINGS, \
                                        BOOK_STRINGS


class CitationFactory():
    """Creates a ready to use Citation when given a CitationType.
    Citation object contains all CitationAttributes that are needed for the type.
    """
    @staticmethod
    def get_new_citation(citation_type: CitationType):
        """Returns a new Citation object that matches the CitationType given.
        """
        match citation_type:
            case CitationType.ARTICLE:
                return Citation(citation_type, ARTICLE_STRINGS)
            case CitationType.INPROCEEDINGS:
                return Citation(citation_type, INPROCEEDINGS_STRINGS)
            case _:
                return Citation(citation_type, BOOK_STRINGS)
