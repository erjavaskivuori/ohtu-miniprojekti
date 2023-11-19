import unittest
from entities.citation import Citation

class TestCitation(unittest.TestCase):
    def setUp(self):
        self.citation = Citation("a","a","a",11)

    def test_constrcutor_works(self):
        output = str(self.citation)
        self.assertEqual(output,"a, a, a, 11")