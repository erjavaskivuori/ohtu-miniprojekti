import unittest
from citations.citation_factory import CitationFactory
from citations.new_citation import Citation, CitationType, CitationAttribute
from citations.citation_strings import BOOK_STRINGS, ARTICLE_STRINGS, INPROCEEDINGS_STRINGS
from citations.bibtex_maker import BibTexMaker

class TestBibtexMaker(unittest.TestCase):
    
    def test_fail_making_file(self):
        citation = {"asd", CitationFactory.get_new_citation(CitationType.BOOK)}
        self.assertFalse(BibTexMaker.try_generate_bible_text_file(citation, "???"))

    def test_create_file(self):
        citation = {}
        citation[0] = CitationFactory.get_new_citation(CitationType.BOOK)
        self.assertTrue(BibTexMaker.try_generate_bible_text_file(citation, "src/tests/bibtest"))
        
    