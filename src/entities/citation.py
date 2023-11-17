

class Citation:
    def __init__(self, type:str, author:str, title:str, year:int):
        self.type = type
        self.author = author
        self.title = title
        self.year = year

        self.__input_valid()

    def __input_valid(self):
        if type(self.year) != int:
            raise ValueError("Type must be integer")
        if self.year < 0:
            raise ValueError("Year can't be negative")

    def __str__(self):
        return f"{self.type}, {self.author}, {self.title}, {self.year}"
    
