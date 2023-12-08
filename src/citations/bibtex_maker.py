import os
from citations.new_citation import Citation, CitationType

WRITE_COMMAND = "w+"
ILLEGAL_CHARACTERS = "#%{&}<>*?$!:'@+`|="
BIBFILE_TARGET_FOLDER = "bibtex_files"
DOT_BIB = ".bib"
UTF_8 = "utf-8"


class BibTexMaker():
    """Creates .bib files. Usage:
    1: Import BibTexMaker
    2: Call BibTexMake.generate_bible_text_file(citation_dictionary, file name)
    3: ???
    4: File appears in the bibtex_files folder
    """

    @staticmethod
    def try_generate_bible_text_file(citations_dictionary, file_name: str):
        """
        Creates a file ending with .bib from a dictionary of citations objects. 
        Given filename should not contain the ".bib" substring at the end.
        File appears in the bibtex_files folder.
        """
        if any(elem in file_name for elem in ILLEGAL_CHARACTERS):
            return False
        file_name = os.path.join(BIBFILE_TARGET_FOLDER, file_name + DOT_BIB)
        try:
            with open(file_name, WRITE_COMMAND, encoding=UTF_8) as text_file:
                text = ""
                for key in citations_dictionary:
                    text += BibTexMaker.__generate_citation_text(
                        citations_dictionary[key])
                text_file.write(text)
                return True
        except IOError as e:
            print(e)
        return False

    @staticmethod
    def __generate_citation_text(citation: Citation):
        """Returns a .bib format string from a citation object.
        """
        start = "@" + CitationType(citation.type).name.lower() + \
            "{" + citation.label + ",\n"
        middle = ""
        for attribute in citation.attributes:
            middle += attribute.get_name()
            middle += " = {" + str(attribute.get_value()) + "},\n"
        end = "}\n\n"
        return start + middle + end
