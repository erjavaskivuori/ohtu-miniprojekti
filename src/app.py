""" app.py - The main application """

from logic.citation_manager import CitationManager
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

            if action == "\0": # Fast escape used ony by tests
                break
            if action == Commands.QUIT:
                break
            if action == Commands.ADD:
                if not self._cm.add_citation_by_user_input():
                    self._tui.print_error("Viitten lisäys ei onnistunut")
            if action == Commands.LIST:
                self._cm.print_all()
            if action == Commands.HELP:
                self._tui.help()
            if action == Commands.TAG:
                pass
            if action == Commands.BIB:
                self._cm.create_bib_file()
            if action == Commands.SEARCH:
                pass


if __name__ == "__main__":
    app = App()
    app.run()
