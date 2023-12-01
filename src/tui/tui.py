
""" TEXT USER INTERFACE - Module for user actions in text mode """
from enum import Enum


class Commands(Enum):
    """ Commands """
    QUIT =	0
    ADD =	1
    LIST =	2
    HELP =	3
    TAG =	4
    BIB =	5
    SEARCH =	6

class ANSI:
    reset=	"\033[0m"
    bold=	"\033[1m"
    red=	"\033[31m"
    green=	"\033[32m"
    magenta=	"\033[35m"


class Tui():
    """ Tui - Class for menu and user inputs in text mode """

    greetings = ANSI.green+"*** TERVETULOA BIBSELLIIN ***"+ANSI.reset+"""

Luo, lajittele, muokkaa viitteitä ja vedosta niistä BiBTeX tiedosto.
"""

    usage = """
Ohjelmaa käytetään niin, että valikossa syötetään toiminto.
Valittu toiminto sitten kyselee toiminnon suorittamiseen
tarvittavat tiedot."""

    commands = {
        'lopeta':	Commands.QUIT,
        'poistu':	Commands.QUIT,
        'pois':		Commands.QUIT,
        'lisää':	Commands.ADD,
        'listaa':	Commands.LIST,
        'menu':		Commands.HELP,
        'apua':		Commands.HELP,
        'auta':		Commands.HELP,
        'tägää':	Commands.TAG,
        'luo':		Commands.BIB,
        'hae':		Commands.SEARCH
    }

    descriptions = {
        Commands.QUIT:		"Lopeta ohjelma",
        Commands.ADD:		"Lisää viite",
        Commands.LIST:		"Listaa viitteet",
        Commands.HELP:		"Tulosta valikko/ohjeet",
        Commands.TAG:		"Anna viitteelle tagi",
        Commands.BIB:		"Kirjoita viiteluettelo BiBTeX muodossa",
        Commands.SEARCH:	"Hae viitteet tägillä"
    }

    categories = {
        "Lisää ja päivitä":	[Commands.ADD, Commands.TAG],
        "Näytä":		[Commands.LIST, Commands.SEARCH],
        "Sekalaista":		[Commands.HELP],
        "Tallenna & Lopeta":	[Commands.QUIT, Commands.BIB]
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
            self.output(f"\n  {ANSI.bold}{cat}{ANSI.reset}\n")

            for desc in cmd_in_cat:
                keys = []
                for key, cmd in self.commands.items():
                    if cmd == desc:
                        keys.append(key)
                self.output(f"   {keys[0]:8s}   {self.descriptions[desc]:40s}")
                self.output(f"[myös: {', '.join(keys[1:])}]\n"
                        if len(keys) > 1 else "\n")
        self.output("\n")

    def menu(self):
        """ menu() - prints out menu prompt and demands valid command """
        while True:
            self.output("\nKomento (apu: syötä menu): ")
            try:
                key = self.input()
            except EOFError:		# Make Ctrl-D work exit
                self.output("\n")
                key = "\0"
            except KeyboardInterrupt:	# Make Ctrl-C reset input
                self.output("\n")
                continue
            if key == "\0": # Fast escape used ony by tests
                return "\0"
            if key in self.commands:
                break
            self.print_error(f"{key}: tuntematon komento.")
        return self.commands[key]

    def ask(self, question: str, validator=lambda a: True):
        """ ask(str, func) - ask user for input and validates it 
        
            str:	String to output before asking for input
            func:	Validator function for the sting.
                        Defaults to the one which returns always true.
        
        """
        while True:
            self.output(f"\nSyötä {question}: ")
            a = self.input()
            if a == "\0": # Fast escape used ony by tests
                return "\0"
            if a != "" and validator(a):
                break
            self.print_error(f"Syöte '{a}' ei kelpaa.")
        return a


    def print_item_entry(self, cite_id :str, txt :str):
        """ print_item_entry() - For printing identifying line of citation"""
        self.output(f"{ANSI.magenta}id:{cite_id}\t{txt}{ANSI.reset}\n")


    def print_item_attribute(self, key :str, value :str):
        """ print_item_attribute(key, value) -
                    for printing attributes of citation just after id line"""
        self.output(f"\t{key+':':14s}{value}\n")


    def print(self, msg :str):
        """ print(msg) - Just for printing plain text """
        self.output(str(msg)+"\n")


    def print_error(self, msg :str):
        """ print_error(msg) - For printing ERROR messages in RED color """
        self.output(f"{ANSI.red}*** VIRHE: {msg}{ANSI.reset}\n")
