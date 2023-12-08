import unittest
from citations.new_citation import Citation, CitationAttribute

class CitationAttributeStrTests(unittest.TestCase):

    def test_citation_attribute_to_str(self):
        ca = CitationAttribute("moikka")
        self.assertEqual( "moikka: ", str(ca) )


class CitationStrTests(unittest.TestCase):
    
    def test_citation_to_str(self):
        c = Citation( 1, ["atribuutti"])
        self.assertIn( "atribuutti", str(c) )