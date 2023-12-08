from citations.new_citation import Citation, CitationType

WRITE_COMMAND = "w+"
ILLEGAL_CHARACTERS = "#%{&}<>*?$!:'@+`|="
class BibTexMaker():
    """Creates .bib files. Usage:
    1: Import BibTexMaker
    2: Call BibTexMake.generate_bible_text_file(citation_dictionary, file name)
    3: ???
    4: File appears in the project root folder
    """

    @staticmethod
    def try_generate_bible_text_file(citations_dictionary, file_name: str):
        """
        Creates a file ending with .bib from a dictionary of citations objects. 
        Given filename should not contain the ".bib" substring at the end.
        """
        if any(elem in file_name for elem in ILLEGAL_CHARACTERS):
            return False
        try:
            with open(file_name + ".bib", WRITE_COMMAND, encoding="utf-8") as text_file:
                text = ""
                for key in citations_dictionary:
                    print(citations_dictionary[key])
                    text += BibTexMaker.__generate_citation_text(citations_dictionary[key])
                text_file.write(text)
                return True
        except IOError as e:
            print(e)
        return False

    @staticmethod
    def __generate_citation_text(citation: Citation):
        """Returns a .bib format string from a citation object.
        """
        start = "@" + CitationType(citation.type).name.lower() + "{" + citation.label + ",\n"
        middle = ""
        for attribute in citation.attributes:
            middle += attribute.get_name()
            middle += " = {" + str(attribute.get_value()) + "},\n"
        end = "}\n\n"
        return start + middle + end
