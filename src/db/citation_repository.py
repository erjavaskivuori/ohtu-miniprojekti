from database_connection import form_database_connection
from citations.new_citation import Citation, CitationType, CitationAttribute
from citations.citation_factory import AUTHOR, TITLE, YEAR, JOURNAL_TITLE, BOOK_TITLE


class CitationRepository():

    def __init__(self, connection: form_database_connection):
        """Luokan kontruktori.

        Args:
            connection: Tietokantayhteyden Connection-olio.
        """

        self._connection = connection

    def create_citation(self, citation: Citation):
        attributes = citation.get_attributes_dictionary()
        print(attributes)
        cursor = self._connection.cursor()
        cursor.execute("""INSERT INTO citations (type, author, title, year, journal_title, book_title)
                       VALUES (?, ?, ?, ?, ?, ?)""",
                       [citation.type.name, attributes.get(AUTHOR, ""), attributes.get(TITLE, ""), attributes.get(YEAR, ""), \
                          attributes.get(JOURNAL_TITLE, ""), attributes.get(BOOK_TITLE, "")])

        self._connection.commit()

    def get_one_citation(self, title: str):
        """Hakee yhden sitaatin.

        Args:
            title (str): title, jonka perusteella sitaatti haetaan

        Returns:
            _type_: Sitatti, joka vastaa hakua. None jos sitaattia ei löydy.
        """
        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT type, author, title, year FROM citations WHERE title = ?",
            [title])
        row = cursor.fetchone()

        if row is None:
            return None

        return Citation(row[0], row[1], row[2], row[3])

    def get_all_citations(self):
        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT type, author, title, year FROM citations")
        rows = cursor.fetchall()

        return [Citation(row[0], row[1], row[2], row[3]) for row in rows]

    def clear_table(self):
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM citations")
        self._connection.commit()

citation_repository = CitationRepository(form_database_connection())
