from enum import Enum


class Commands(Enum):
    QUIT = 0,
    ADD = 1,
    LIST = 2,
    HELP = 3


class Tui:
    """ Tui - Class for menu and user inputs in text mode """

    greetings = """
*** TERVETULOA BIBSELLIIN ***

Luo, lajittele, muokkaa viitteitä ja vedosta niistä BiBTeX tiedosto.

"""

    usage = """
Ohjelma toimii syöttämällä valikossa toimintoa vastaava yksittäinen kirjain.
Näin valittu toiminto sitten kysyy käyttäjältä tarvittavat tiedot.
"""

    commands = {
        'Q': Commands.QUIT,
        'q': Commands.QUIT,
        'A': Commands.ADD,
        'a': Commands.ADD,
        'L': Commands.LIST,
        'l': Commands.LIST,
        'P': Commands.LIST,
        'p': Commands.LIST,
        'H': Commands.HELP,
        'h': Commands.HELP,
        '?': Commands.HELP
    }

    descriptions = {
        Commands.QUIT: "Lopeta ohjelma",
        Commands.ADD: "Lisää viite",
        Commands.LIST: "Listaa viitteet",
        Commands.HELP: "Tulosta ohjeet"
    }

    def __init__(self):
        print(self.greetings)
        self.help()

    def help(self):
        print(self.usage)
        print("Komento:        Toiminto:")
        for desc in self.descriptions.keys():
            keys = ""
            for comm in self.commands:
                if self.commands[comm] == desc:
                    keys += f"[{comm}]"
            print(f"{keys:16s}{self.descriptions[desc]}")

    def menu(self):
        while True:
            key = input("(VALIKKO) Anna komento: ")
            if key in self.commands.keys():
                break
            print(f"Komento {key} ei kelpaa. Anna [?][h][H] saadaksesi apua.")
        return self.commands[key]

    def ask(self, question: str, validator=lambda a: True):
        while True:
            a = input(f"Anna {question}: ")
            if a != "" and validator(a):
                break
            print(f"Syöte ei kelpaa")
        return a


if __name__ == "__main__":
    pass
