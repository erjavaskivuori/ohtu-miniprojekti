import unittest
from logic.citation_manager import CitationManager
from entities.citation import Citation
from tui.tui import Tui
from tui.tui_io import TuiIO


class TestCitationManager(unittest.TestCase):
    def setUp(self):
        self.manager = CitationManager(Tui(TuiIO()))
        self.manager.clear_all()  # Clear database before tests
        self.citation = Citation("a", "a", "a", 11)
        self.citation2 = Citation("b", "b", "b", 12)

    def test_add_one_citation(self):
        self.manager.add_citation(self.citation)
        citation = self.manager.return_one_citation(self.citation.title)
        self.assertEqual(citation.title, self.citation.title)

    def test_add_two_citations(self):
        self.manager.add_citation(self.citation)
        self.manager.add_citation(self.citation2)
        citation = self.manager.return_one_citation(self.citation.title)
        citation2 = self.manager.return_one_citation(self.citation2.title)
        self.assertEqual(citation.title, self.citation.title)
        self.assertEqual(citation2.title, self.citation2.title)

    def test_get_one_citation_which_does_not_exists(self):
        self.manager.add_citation(self.citation)
        citation = self.manager.return_one_citation("c")
        self.assertEqual(citation, None)

    def test_return_all_citations(self):
        self.manager.add_citation(self.citation)
        self.manager.add_citation(self.citation2)
        # self.assertEqual(self.manager.return_all_citaions(),
        #                 [self.citation, self.citation2])
        self.assertEqual(len(self.manager.return_all_citaions()), 2)

    def test_print_all(self):
        self.manager.add_citation(self.citation)
        self.manager.add_citation(self.citation2)
        self.assertEqual(self.manager.print_all(), None)
