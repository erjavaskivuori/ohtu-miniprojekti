from database_connection import form_database_connection
from entities.citation import Citation

class CitationRepository():

    def __init__(self, connection: form_database_connection):
        """Luokan kontruktori.

        Args:
            connection: Tietokantayhteyden Connection-olio.
        """

        self._connection = connection

    def create_citation(self, type, author, title, year):
        cursor = self._connection.cursor()
        cursor.execute("""INSERT INTO citations (typer, author, title, year) 
                       VALUES (?, ?, ?, ?)""", \
                        [type, author, title, year])
        
        self._connection.commit()

        return Citation(type, author, title, year)
    
    def get_all_citations(self):
        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT * FROM citations")
        rows = cursor.fetchall()

        return [Citation(row[0], row[1], row[2], row[3]) for row in rows]