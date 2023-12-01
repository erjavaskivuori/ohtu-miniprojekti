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
ARTICLE_STRINGS = [AUTHOR, TITLE, YEAR, JOURNAL_TITLE]
# Requiredfields: author,title,booktitle,year/date
INPROCEEDINGS_STRINGS = [AUTHOR, TITLE, YEAR,  BOOK_TITLE]
# --------------------------------------

ATTR_TRANSLATIONS = {
    AUTHOR:		"tekijä",
    TITLE:		"otsikko",
    YEAR:		"vuosi",
    JOURNAL_TITLE:	"lehden nimi",
    BOOK_TITLE:		"kirjan nimi"
}

# Biblatex documentation:
# http://mirrors.ctan.org/macros/latex/contrib/biblatex/doc/biblatex.pdf
# (Entry types, starting from page 9)
# Example, Book:
# Requiredfields: author,title,year/date
# Optional fields: editor,editora,editorb,editorc,translator,
#   annotator,commentator,introduction,foreword,afterword, subtitle,
#   titleaddon,maintitle,mainsubtitle,maintitleaddon, language,
#   origlanguage,volume,part,edition,volumes,series, number,note,publisher,
#   location,isbn,eid,chapter,pages, pagetotal,addendum,pubstate,doi,eprint,eprintclass,
#   eprinttype,url,urldate
