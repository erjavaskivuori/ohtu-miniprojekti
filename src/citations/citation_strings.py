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


