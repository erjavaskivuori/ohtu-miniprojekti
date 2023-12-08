import sqlite3
import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
# pylint: disable=C0413
from config import DATABASE_FILE_PATH, POPULATE_CITATIONS_PATH


def populate_citations_from_file(connection, file_path):
    """Populate the 'citations' table with test data from a text file.

    Args:
        connection: SQLite database Connection object.
        file_path (str): Path to the text file containing citation data.
    """
    cursor = connection.cursor()

    with open(file_path, 'r', encoding='utf8') as file:
        for line in file:
            values = line.strip().split(',')

            cursor.execute("""
                INSERT INTO citations (label, type, author, title, year, journal_title, book_title)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, values)

    connection.commit()


if __name__ == "__main__":
    conn = sqlite3.connect(DATABASE_FILE_PATH)
    populate_citations_from_file(conn, POPULATE_CITATIONS_PATH)
    conn.close()
