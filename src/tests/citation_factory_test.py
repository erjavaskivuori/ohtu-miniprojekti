import unittest
from citations.citation_factory import CitationFactory
from citations.new_citation import Citation, CitationType, CitationAttribute
from citations.citation_strings import BOOK_STRINGS, ARTICLE_STRINGS, INPROCEEDINGS_STRINGS

class TestCitationFactory(unittest.TestCase):
    
    def test_can_create_book(self):
        citation = CitationFactory.get_new_citation(CitationType.BOOK)
        dictionary = citation.get_attributes_dictionary()
        for string in BOOK_STRINGS:
            self.assertEqual(string in dictionary, True)
    
    def test_can_create_article(self):
        citation = CitationFactory.get_new_citation(CitationType.ARTICLE)
        dictionary = citation.get_attributes_dictionary()
        for string in ARTICLE_STRINGS:
            self.assertEqual(string in dictionary, True)
    
    def test_can_create_inproceedings(self):
        citation = CitationFactory.get_new_citation(CitationType.INPROCEEDINGS)
        dictionary = citation.get_attributes_dictionary()
        for string in INPROCEEDINGS_STRINGS:
            self.assertEqual(string in dictionary, True)
        