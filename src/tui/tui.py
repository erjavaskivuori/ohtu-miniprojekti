""" TEXT USER INTERFACE - Module for user actions in test mode """
from enum import Enum

class Commands(Enum):
    """ Commands """
    QUIT = 0
    ADD = 1
    LIST = 2
    HELP = 3

class Tui:
    """ Tui - Class for menu and user inputs in text mode """

    greetings = "\033[32m*** TERVETULOA BIBSELLIIN ***\033[39m"+"""

Luo, lajittele, muokkaa viitteitä ja vedosta niistä BiBTeX tiedosto.
"""

    usage = """
Ohjelman käyttöliittymä mukailee jokaisen suosikkiohjelma fdisk:iä.
Ohjelmaa siis käytetään niin, että valikossa syötetään toimintoa vastaava
yksittäinen kirjain. Valittu toiminto sitten kyselee toiminnon suorittamiseen
tarvittavat tiedot."""

    commands = {
        'lopeta': Commands.QUIT,
        'lisää': Commands.ADD,
        'listaa': Commands.LIST,
        'menu': Commands.HELP,
        'apua': Commands.HELP,
        'auta': Commands.HELP
    }

    descriptions = {
        Commands.QUIT: "Lopeta ohjelma",
        Commands.ADD: "Lisää viite",
        Commands.LIST: "Listaa viitteet",
        Commands.HELP: "Tulosta valikko/ohjeet"
    }

    categories = {
        "Viitteet": [Commands.ADD, Commands.LIST],
        "Sekalaista": [Commands.HELP],
        "Tallenna & Lopeta": [Commands.QUIT]
    }

    def __init__(self):
        print(self.greetings)

    def help(self):
        """ help() - prints out usage and command information """
        print(self.usage)
        print("\nApu:")
        for cat, cmd_in_cat in self.categories.items():
            print(f"\n  \033[1m{cat}\033[0m")

            for desc in cmd_in_cat:
                keys = []
                for key, cmd in self.commands.items():
                    if cmd == desc:
                        keys.append(key)
                print(f"   {keys[0]:6s}   {self.descriptions[desc]:40s}", end="")
                print(f"[myös: {', '.join(keys[1:])}]" if len(keys)>1 else "")
        print()

    def menu(self):
        """ menu() - prints out menu prompt and demands valid command """
        while True:
            key = input("\nKomento (apu: syötä menu): ")
            if key in self.commands:
                break
            print(f"\033[31m{key}: tuntematon komento.\033[0m")
        return self.commands[key]

    def ask(self, question: str, validator=lambda a: True):
        """ ask(str, function) - ask user for input and validates it """
        while True:
            a = input(f"\nSyötä {question}: ")
            if a != "" and validator(a):
                break
            print(f"\033[31mSyöte '{a}' ei kelpaa.\033[0m")
        return a
