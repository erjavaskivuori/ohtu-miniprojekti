from db.connection import form_database_connection


class TagRepository():
    def __init__(self, connection: form_database_connection):
        """Constructor.

        Args:
            connection: Databases Connection-object.
        """

        self._connection = connection

    def create_new_tag(self, tag):

        all_tags = self.get_all_tags()

        if tag not in all_tags:
            cursor = self._connection.cursor()
            cursor.execute("""INSERT INTO tags (tag) VALUES (?)""", [tag])
            self._connection.commit()

            return cursor.lastrowid
        return all_tags[tag]

    def add_tag_to_citation(self, citation_id, tag):
        tag_id = self.create_new_tag(tag)

        cursor = self._connection.cursor()
        cursor.execute("""INSERT INTO tagged (tag_id, citation_id) VALUES (?, ?)""", [
                       tag_id, citation_id])
        self._connection.commit()
        return True

    def tag_by_citation_id(self, citation_id):
        cursor = self._connection.cursor()
        cursor.execute("""SELECT t.tag FROM tags t LEFT JOIN tagged td
                    ON t.id=td.tag_id WHERE td.citation_id=?""", [citation_id])
        rows = cursor.fetchall()
        return rows

    def get_all_tags(self):

        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT id, tag FROM tags")
        rows = cursor.fetchall()

        tags = {}

        for row in rows:
            tags[row[1]] = row[0]

        return tags

    def clear_tables(self):
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM tags")
        cursor.execute("DELETE FROM tagged")
        self._connection.commit()

    def delete_by_citation_id(self, citation_id):
        cursor = self._connection.cursor()
        cursor.execute("""DELETE FROM tagged
                       WHERE citation_id=?
                       """,[citation_id])
        self._connection.commit()

tag_repository = TagRepository(form_database_connection())
