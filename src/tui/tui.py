from enum import Enum

class Commands(Enum):
    QUIT = 0,
    ADD = 1,
    LIST = 2,
    HELP = 3

class Tui:
    """ Tui - Class for menu and user inputs in text mode """

    greetings = """
[32m*** TERVETULOA BIBSELLIIN ***[39m

Luo, lajittele, muokkaa viitteitä ja vedosta niistä BiBTeX tiedosto.

"""

    usage = """
Ohjelman käyttöliittymä mukailee jokaisen suosikkiohjelma fdisk:iä.
Ohjelmaa siis käytetään niin, että valikossa syötetään toimintoa vastaava
yksittäinen kirjain. Valittu toiminto sitten kyselee toiminnon suorittamiseen
tarvittavat tiedot.
"""

    commands = {
        'q': Commands.QUIT,
        'a': Commands.ADD,
        'p': Commands.LIST,
        'l': Commands.LIST,
        'm': Commands.HELP,
        'h': Commands.HELP,
        '?': Commands.HELP
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
        print(self.usage)
        print("\nApu:")
        for cat in self.categories:
            print(f"\n  {cat}:")
        
            for desc in self.categories[cat]:
                keys = []
                for comm in self.commands:
                    if self.commands[comm] == desc:
                        keys.append(comm)
                print(f"   {keys[0]}   {self.descriptions[desc]:40s}", end="")
                print(f"[myös: {', '.join(keys[1:])}]" if len(keys)>1 else "")

    def menu(self):
        while True:
            key = input("\nKomento (apu: syötä m): ")
            if key in self.commands.keys():
                break
            print("""[31m"""f"{key}: tuntematon komento.""""[39m""")
        return self.commands[key]

    def ask(self, question: str, validator=lambda a: True):
        while True:
            a = input(f"\nSyötä {question}: ")
            if a != "" and validator(a):
                break
            print("""[31m"""f"Syöte '{a}' ei kelpaa.""""[39m""")
        return a

