"""Luokka, joka luo uuden sitaattiolion"""


class Citation():
    def __init__(self, citation_type: str, author: str, title: str, year: int):
        self.type = citation_type
        self.author = author
        self.title = title
        self.year = year

    @staticmethod
    def year_validator(year):
        try:
            i = int(year)
            if i < 0 or i > 2040:
                return False
        except ValueError:
            return False
        return True
    
    def __str__(self):
        return f"{self.type}, {self.author}, {self.title}, {self.year}"
