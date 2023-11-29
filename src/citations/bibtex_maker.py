from new_citation import Citation, CitationType
from citation_factory import CitationFactory

class BibTexMaker():
    
    @staticmethod
    def generate_bible_text_file(citationList: list[Citation], fileName: str):
        textFile = open(fileName + ".bib","w+")
        text = ""
        for citation in citationList:
            text += BibTexMaker.__generate_citation_text(citation)
        ##create textfile
        print(text)

    @staticmethod
    def __generate_citation_text(citation: Citation):
        start = "@" + citation.type.name + "{" + citation.label + ",\n"
        middle = ""
        for attribute in citation.attributes:
            middle += attribute.get_name() + " = {" + attribute.get_value() +"},\n"
        end = "}\n\n"
        return start + middle + end
    
if __name__ == "__main__":
    citations = {CitationFactory.get_new_citation(CitationType.ARTICLE), CitationFactory.get_new_citation(CitationType.BOOK)}
    BibTexMaker.generate_bible_text_file(citations, "bibtesti")