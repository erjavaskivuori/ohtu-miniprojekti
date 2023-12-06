from database_connection import form_database_connection
from citations.new_citation import Citation, CitationType
from citations.citation_factory import CitationFactory
from citations.citation_strings import AUTHOR, TITLE, YEAR, JOURNAL_TITLE, \
                                        BOOK_TITLE



class CitationRepository():

    def __init__(self, connection: form_database_connection):
        """Luokan kontruktori.

        Args:
            connection: Tietokantayhteyden Connection-olio.
        """

        self._connection = connection

    def create_citation(self, citation: Citation):
        attributes = citation.get_attributes_dictionary()
        cursor = self._connection.cursor()
        cursor.execute("""INSERT INTO citations (type, label, author, title, year, \
                        journal_title, book_title)
                       VALUES (?, ?, ?, ?, ?, ?, ?)""",
                       [citation.type.value, citation.label, attributes.get(AUTHOR, ""), \
                        attributes.get(TITLE, ""), attributes.get(YEAR, ""), \
                        attributes.get(JOURNAL_TITLE, ""), \
                        attributes.get(BOOK_TITLE, "")])

        self._connection.commit()

        return cursor.lastrowid

    def get_all_citations(self):
        cursor = self._connection.cursor()
        cursor.execute(
            """SELECT c.id, c.label, c.type, c.author, c.title,
            c.year, c.journal_title, c.book_title, t2.tag
            FROM citations c LEFT JOIN tagged t ON c.id=t.citation_id
            LEFT JOIN tags t2 ON t2.id=t.tag_id
            """)
        rows = cursor.fetchall()

        if rows is None:
            return None

        citations = {}

        for row in rows:
            citation_label = row[1]
            citation_type = row[2]
            citation = CitationFactory.get_new_citation(CitationType(int(citation_type)))
            citation.set_label(citation_label)
            if row[-1] is not None:
                citation.set_tag(row[-1])

            column = 3

            for attribute in citation.attributes:
                while column < len(row) and row[column] == '':
                    column += 1
                    if column == len(row):
                        break
                if column == len(row):
                    break
                attribute.set_value(row[column])
                column += 1

            citations[row[0]] = citation
        return citations

    def delete_citation(self, citation_id):
        cursor = self._connection.cursor()
        cursor.execute("""DELETE FROM citations WHERE id=?
        """,[citation_id])
        self._connection.commit()

    def clear_table(self):
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM citations")
        self._connection.commit()

    def is_label_already_used(self, label: str):
        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT * FROM citations WHERE label=?", [label])
        rows = cursor.fetchone()
        if rows is not None:
            return True
        return False

citation_repository = CitationRepository(form_database_connection())
