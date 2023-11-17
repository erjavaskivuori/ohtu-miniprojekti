from enum import Enum

usage = """ *** TERVETULOA BIB ***

Käyttö:

Valikko toimii antamalla kirjaimen ja toimimalla ohjeiden mukaan..

kirjoita tähn jotain järkevää
"""

class Commands(Enum):
    QUIT = 0,
    ADD = 1,
    LIST = 2,
    HELP = 3

commands = {
    'Q'	: Commands.QUIT,
    'q'	: Commands.QUIT,
    'A'	: Commands.ADD,
    'a'	: Commands.ADD    
}

class Tui:
    def __init__(self):
        print(usage)
        
    def menu(self):
        while True:
            key = input("Anna komento: ")
            if key in commands.keys():
                break
            print(f"Komento {key} ei kelpaa")
        return commands[key]
        
    def ask(self, question :str, validator = lambda a: True):
        while True:
            a = input(f"Anna {question}: ")
            if a != "" and validator(a):
                break
            print(f"Syöte ei kelpaa")
        return a



            
        
if __name__ == "__main__":
    pass