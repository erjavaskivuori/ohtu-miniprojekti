from citations.citation_type import CitationType
from citations.new_citation import Citation 

# named in a way that .bib accepts
# Could be moved to a file of it's own
AUTHOR = "author"
TITLE = "title"
YEAR = "year"
JOURNAL_TITLE = "journaltitle"
BOOK_TITLE = "booktitle"

# Requiredfields: author,title,year/date
BOOK_STRINGS = [AUTHOR, TITLE, YEAR]
# Requiredfields: author,title,journaltitle,year/date
ARTICLE_STRINGS = [AUTHOR, TITLE, JOURNAL_TITLE, YEAR]
# Requiredfields: author,title,booktitle,year/date
INPROCEEDINGS_STRINGS = [AUTHOR, TITLE, BOOK_TITLE, YEAR]
# --------------------------------------

class CitationFactory:
    
    def get_new_citation(self, type: CitationType):
        #hopefully temporary "if else hell":
        match type:
            case CitationType.BOOK:
                return Citation(type, BOOK_STRINGS)
            case CitationType.ARTICLE:
                return Citation(type, ARTICLE_STRINGS)
            case CitationType.INPROCEEDINGS:
                return Citation(type, INPROCEEDINGS_STRINGS)
        #default to book for now
        return Citation(type, BOOK_STRINGS)
    
    
        
#Biblatex documentation: 
#http://mirrors.ctan.org/macros/latex/contrib/biblatex/doc/biblatex.pdf
#(Entry types, starting from page 9)
#Example, Book: 
# Requiredfields: author,title,year/date
# Optional fields: editor,editora,editorb,editorc,translator, 
#   annotator,commentator,introduction,foreword,afterword, subtitle,
#   titleaddon,maintitle,mainsubtitle,maintitleaddon, language,
#   origlanguage,volume,part,edition,volumes,series, number,note,publisher,
#   location,isbn,eid,chapter,pages, pagetotal,addendum,pubstate,doi,eprint,eprintclass, 
#   eprinttype,url,urldate