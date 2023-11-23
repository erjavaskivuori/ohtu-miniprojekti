
""" TEXT USER INTERFACE - Module for user actions in test mode """
from enum import Enum


class Commands(Enum):
    """ Commands """
    QUIT = 0
    ADD = 1
    LIST = 2
    HELP = 3


class Tui():
    """ Tui - Class for menu and user inputs in text mode """

    greetings = "\033[32m*** TERVETULOA BIBSELLIIN ***\033[39m"+"""

Luo, lajittele, muokkaa viitteitä ja vedosta niistä BiBTeX tiedosto.
"""

    usage = """
Ohjelmaa käytetään niin, että valikossa syötetään toimintoa vastaava
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

    def __init__(self, io):
        self.input = io.input
        self.output = io.output

    def greet(self):
        """ greet() - greets user """
        self.output(self.greetings)

    def help(self):
        """ help() - prints out usage and command information """
        self.output(self.usage)
        self.output("\nApu:\n")
        for cat, cmd_in_cat in self.categories.items():
            self.output(f"\n  \033[1m{cat}\033[0m\n")

            for desc in cmd_in_cat:
                keys = []
                for key, cmd in self.commands.items():
                    if cmd == desc:
                        keys.append(key)
                self.output(f"   {keys[0]:6s}   {self.descriptions[desc]:40s}")
                self.output(f"[myös: {', '.join(keys[1:])}]\n" if len(
                    keys) > 1 else "\n")
        self.output("\n")

    def menu(self):
        """ menu() - prints out menu prompt and demands valid command """
        while True:
            self.output("\nKomento (apu: syötä menu): ")
            key = self.input()
            if key == "\0":
                return "\0";
            if key in self.commands:
                break
            self.output(f"\033[31m{key}: tuntematon komento.\033[0m\n")
        return self.commands[key]

    def ask(self, question: str, validator=lambda a: True):
        """ ask(str, function) - ask user for input and validates it """
        while True:
            self.output(f"\nSyötä {question}: ")
            a = self.input()
            if a == "\0":
                return "\0"
            if a != "" and validator(a):
                break
            self.output(f"\033[31mSyöte '{a}' ei kelpaa.\033[0m\n")
        return a

    def list_all(self):
        """kirjoitetaan ouputtiin 'lista kaikista', jotta voidaaa testata,
        robot frmaeworkin avulla."""
        self.output("lista kaikista")
        info_message = """\nJos haluat listata viitteet tietokannasta,
        kommentoi pois App.py:stä self.cm.print_all()"""
        self.output(info_message)
        
    def print_item_entry(self, id :str, txt :str):
        self.output(f"[id={id}]\t{txt}\n")
    
    def print_item_attribute(self, key :str, value :str):
        self.output(f"\t{key%12}:{value}\n")
    
    def print(self, msg :str):
        self.output(msg)
        self.output("\n")
    
    def print_error(self, msg :str):
        self.output("\033[31m*** VIRHE: "+msg+"\033[0m")
        self.output("\n")
    
