import unittest
from logic.citation_manager import CitationManager
from entities.citation import Citation


class TestCitationManager(unittest.TestCase):
    def setUp(self):
        self.manager = CitationManager()
        self.citation = Citation("a", "a", "a", 11)
        self.citation2 = Citation("b", "b", "b", 12)

    def test_add_one_citation(self):
        self.manager.add_citation(self.citation)
        self.assertEqual(len(self.manager.all), 1)

    def test_add_twon_citations(self):
        self.manager.add_citation(self.citation)
        self.manager.add_citation(self.citation2)
        self.assertEqual(len(self.manager.all), 2)

    def test_return_all_citations(self):
        self.manager.add_citation(self.citation)
        self.manager.add_citation(self.citation2)
        self.assertEqual(self.manager.return_all_citaions(),
                         [self.citation, self.citation2])

    def test_print_all(self):
        self.manager.add_citation(self.citation)
        self.manager.add_citation(self.citation2)
        self.assertEqual(self.manager.print_all(), None)
