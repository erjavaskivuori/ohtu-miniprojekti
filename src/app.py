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
            match self._tui.menu():
                case Commands.ADD:
                    if not self._cm.add_citation_by_user_input():
                        self._tui.print_error("Viitten lisäys ei onnistunut")
                    continue
                case Commands.LIST:
                    self._cm.print_all()
                    continue
                case Commands.HELP:
                    self._tui.help()
                    continue
                case Commands.TAG:
                    if not self._cm.add_tag_for_citation_by_user_input():
                        self._tui.print_error("Tagin lisäys ei onnistunut")
                    continue
                case Commands.BIB:
                    self._cm.create_bib_file()
                    continue
                case Commands.SEARCH:
                    self._cm.print_by_tag()
                    continue
                case Commands.QUIT | "\0":  # Fast escape used for tests
                    break
                case _:
                    self._tui.print_error("Komentoa ei ole implementoitu")


if __name__ == "__main__":
    app = App()
    app.run()
