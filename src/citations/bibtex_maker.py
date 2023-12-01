from citations.new_citation import Citation, CitationType

WRITE_COMMAND = "w+"

class BibTexMaker():
    """Luo .bib tiedostoja. Käyttö:
    1: Importtaa BibTexMaker
    2: Kutsu BibTexMake.generate_bible_text_file(sitaattilista, filun nimi)
    3: ???
    4: Tiedosto ilmestyy /src kansioon
    """

    @staticmethod
    def generate_bible_text_file(citations, file_name: str):
        """
        Luo .bib päätteisen tekstitiedoston listasta Citation olioita. 
        Annetun filenamen ei tarvitse/kannata sisältää .bib päätettä.
        """
        with open(file_name + ".bib", WRITE_COMMAND, encoding="utf-8") as text_file:
            text = ""
            for key in citations:
                print(citations[key])
                text += BibTexMaker.__generate_citation_text(citations[key])
            text_file.write(text)
            
        return True # TODO: Return false if failed

    @staticmethod
    def __generate_citation_text(citation: Citation):
        """Luo yhden sitaatin bibtex formaatissa, palauttaa str.
        """
        start = "@" + CitationType(citation.type).name.lower() + "{" + citation.label + ",\n"
        middle = ""
        for attribute in citation.attributes:
            middle += attribute.get_name() + \
                " = {" + attribute.get_value() + "},\n"
        end = "}\n\n"
        return start + middle + end
