""" app.py - The main application """

from logic.citation_manager import CitationManager
from entities.citation import Citation
from tui.tui import Tui, Commands
from tui.tui_io import TuiIO


class App:
    """ THE APPLICATION !!! """

    def __init__(self, io=TuiIO()):
        self._tui = Tui(io)
        self._cm = CitationManager(self._tui)

    def run(self):
        """ This starts the application """        
        self._tui.greet()
        while True:

            action = self._tui.menu()

            if action == "\0":
                break
            if action == Commands.QUIT:
                break
            if action == Commands.ADD:
                c = Citation(
                    self._tui.ask("tyyppi"),
                    self._tui.ask("tekijä"),
                    self._tui.ask("otsikko"),
                    self._tui.ask("vuosi", Citation.year_validator)
                )
                self._cm.add_citation(c)

            if action == Commands.LIST:
                # tulostetaan kaikki viitteet CitationManagerin metodilla
                # testaamista ajatellen tuloste pitäisi palauttaa ja kirjoittaa
                # io:lla outputtiin
                #self._tui.list_all()
                self._cm.print_all()
            if action == Commands.HELP:
                self._tui.help()


if __name__ == "__main__":
    app = App()
    app.run()
