from db.connection import form_database_connection


def initialize_database():
    """Initializes database tables"""

    connection = form_database_connection()

    drop_tables(connection)
    create_tables(connection)


def drop_tables(connection):
    """Drops all tables from the database.

    Args:
        connection: Databases Connection-object.
    """

    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS citations;")
    cursor.execute("DROP TABLE IF EXISTS tags;")
    cursor.execute("DROP TABLE IF EXISTS tagged;")

    connection.commit()


def create_tables(connection):
    """Creates the database tables.

    Args:
        connection: Databases Connection-object.
    """

    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS citations (
        id INTEGER PRIMARY KEY,
        label TEXT UNIQUE,
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
