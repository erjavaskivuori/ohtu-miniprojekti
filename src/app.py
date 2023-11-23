""" app.py - The main application """

from logic.citation_manager import CitationManager
from entities.citation import Citation
from tui.tui import Tui, Commands
from tui.tui_io import TuiIO


class App:
    """ THE APPLICATION !!! """

    def __init__(self, io=TuiIO()):
        self.tui = Tui(io)
        self.cm = CitationManager()

    def run(self):
        """ This starts the application """
        while True:

            action = self.tui.menu()

            if action == Commands.QUIT:
                break
            if action == Commands.ADD:
                c = Citation(
                    self.tui.ask("tyyppi"),
                    self.tui.ask("tekijä"),
                    self.tui.ask("otsikko"),
                    self.tui.ask("vuosi", Citation.year_validator)
                )
                self.cm.add_citation(c)
            if action == Commands.LIST:
                #self.cm.print_all()
                self.tui.list_all()
            if action == Commands.HELP:
                self.tui.help()


if __name__ == "__main__":
    app = App()
    app.run()
