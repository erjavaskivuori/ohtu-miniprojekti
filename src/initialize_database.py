from database_connection import form_database_connection


def initialize_database():
    """Alustaa tietokannan taulut."""

    connection = form_database_connection()

    drop_tables(connection)
    create_tables(connection)


def drop_tables(connection):
    """Poistaa tietokannan taulut.

    Args:
        connection: Tietokantayhteyden Connection-olio.
    """

    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS citations;")
    cursor.execute("DROP TABLE IF EXISTS tags;")
    cursor.execute("DROP TABLE IF EXISTS tagged;")

    connection.commit()


def create_tables(connection):
    """Luo tietokannan taulut.

    Args:
        connection: Tietokantayhteyden Connection-olio.
    """

    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS citations (
        id INTEGER PRIMARY KEY,
        type TEXT, 
        author TEXT,
        title TEXT,
        year INTEGER,
        journal_title TEXT,
        book_title TEXT);""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS tags (
        id INTEGER PRIMARY KEY,
        tag TEXT);""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS tagged (
        tag_id INTEGER REFERENCES tags,
        citation_id INTEGER REFERENCES citations);""")

    connection.commit()


if __name__ == "__main__":
    initialize_database()
