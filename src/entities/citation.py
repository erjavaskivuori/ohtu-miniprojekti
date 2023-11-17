"""Luokka, joka luo uuden sitaatin"""

class Citation():
    def __init__(self, type:str, author:str, title:str, year:int):
        self.type = type
        self.author = author
        self.title = title
        self.year = year

    def __str__(self):
        return f"{self.type}, {self.author}, {self.title}, {self.year}"

