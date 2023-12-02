import unittest
from citations.citation_factory import CitationFactory
from citations.new_citation import Citation, CitationType, CitationAttribute
from citations.citation_strings import BOOK_STRINGS, ARTICLE_STRINGS, INPROCEEDINGS_STRINGS
from citations.bibtex_maker import BibTexMaker

class TestBibtexMaker(unittest.TestCase):
    
    def setUp(self):
        self.citations = dict()
        self.citations["asd"] = CitationFactory.get_new_citation(CitationType.BOOK)
    
    def test_fail_making_file(self):
        self.assertFalse(BibTexMaker.try_generate_bible_text_file(self.citations, "???#&*" ))

    def test_create_file(self):
        self.assertTrue(BibTexMaker.try_generate_bible_text_file(self.citations, "src/bibtest"))
        
    