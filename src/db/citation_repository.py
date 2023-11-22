from database_connection import form_database_connection
from entities.citation import Citation

class CitationRepository():

    def __init__(self, connection: form_database_connection):
        """Luokan kontruktori.

        Args:
            connection: Tietokantayhteyden Connection-olio.
        """

        self._connection = connection

    def create_citation(self, citation: Citation):
        cursor = self._connection.cursor()
        cursor.execute("""INSERT INTO citations (type, author, title, year) 
                       VALUES (?, ?, ?, ?)""", \
                        [citation.type, citation.author, citation.title, citation.year])
        
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
            "SELECT * FROM citations WHERE title = ?", [title])
        row = cursor.fetchone()

        if row is None:
            return None

        return Citation(row[0], row[1], row[2], row[3])
    
    
    def get_all_citations(self):
        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT * FROM citations")
        rows = cursor.fetchall()

        return [Citation(row[0], row[1], row[2], row[3]) for row in rows]
    

    def clear_table(self):
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM citations")
        self._connection.commit()

citation_repository = CitationRepository(form_database_connection())