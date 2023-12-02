import unittest
from logic.citation_manager import CitationManager
from citations.new_citation import Citation, CitationType
from tui.tui import Tui
from tui.tui_io import TuiIO

AUTHOR = "author"
TITLE = "title"
YEAR = "year"
JOURNAL_TITLE = "journaltitle"
BOOK_TITLE = "booktitle"

class TestCitationManager(unittest.TestCase):
    def setUp(self):
        self.manager = CitationManager(Tui(TuiIO()))
        self.manager.clear_all()  # Clear database before tests
        self.book = Citation(CitationType(1), [AUTHOR, TITLE, YEAR])
        self.article = Citation(CitationType(2), [AUTHOR, TITLE, YEAR, JOURNAL_TITLE])
        self.inproceedings = Citation(CitationType(3), [AUTHOR, TITLE, YEAR,  BOOK_TITLE])
        self.book.attributes[1].set_value("moi")
        self.article.attributes[1].set_value("jee")
        self.inproceedings.attributes[1].set_value("jeee")
        self.book.attributes[2].set_value(2023)
        self.book.attributes[0].set_value("hello")
        self.inproceedings.attributes[2].set_value(2000)
        self.inproceedings.attributes[3].set_value("moi")
        self.inproceedings.attributes[0].set_value("ok")

    def test_add_one_citation(self):
        self.manager.add_citation(self.book)
        self.assertEqual(self.book.attributes[1].get_value(), "moi")

    def test_add_two_citations(self):
        self.manager.add_citation(self.article)
        self.manager.add_citation(self.inproceedings)
        self.assertEqual(self.article.attributes[1].get_value(),"jee")
        self.assertEqual(self.inproceedings.attributes[1].get_value(),"jeee")

    def test_get_one_citation_which_does_not_exists(self):
        self.manager.add_citation(self.book)
        citation = self.manager.return_one_citation("c")
        self.assertEqual(citation, None)

    def test_get_one_citation(self):
        self.manager.add_citation(self.book)
        self.assertEqual(self.book.attributes[1].get_value(),"moi")
    
    def test_return_all_citations(self):
        self.manager.add_citation(self.book)
        self.manager.add_citation(self.inproceedings)
        # self.assertEqual(self.manager.return_all_citaions(),
        #                 [self.citation, self.citation2])
        self.assertEqual(len(self.manager.return_all_citations()), 2)

    # def test_print_all(self):
    #     self.manager.add_citation(self.book)
    #     self.manager.add_citation(self.article)
    #     self.assertEqual(self.manager.print_all(), None)

    def test_year_validator(self):
        self.assertTrue(self.manager.year_validator(1984))
        self.assertFalse(self.manager.year_validator(-1984))
        self.assertFalse(self.manager.year_validator("höpöhöpö"))
    
    def test_is_int_and_in_range_validator_validator(self):
        self.assertTrue(self.manager.is_int_and_in_range_1_to_3_validator(1))
        self.assertFalse(self.manager.is_int_and_in_range_1_to_3_validator(0))
        self.assertFalse(self.manager.is_int_and_in_range_1_to_3_validator("asd"))
        
    #def test_create_file(self):
    #    self.manager.create_bib_file()
