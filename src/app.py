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
        commands = {
            Commands.ADD:		self.__add,
            Commands.LIST:		self.__list,
            Commands.HELP:		self.__help,
            Commands.TAG:		self.__tag,
            Commands.BIB:		self.__bib,
            Commands.SEARCH:		self.__search,
            Commands.DELETE:		self.__delete,
            Commands.DROP:		self.__drop
        }

        self._tui.greet()

        while True:
            command = self._tui.menu()
            if command in (Commands.QUIT, "\0"):
                break
            if command in commands:
                commands[command]()
            else:
                self._tui.print_error("Komentoa ei ole implementoitu")
                break

    def __bib(self):
        self._cm.create_bib_file()

    def __search(self):
        self._cm.print_by_tag()

    def __help(self):
        self._tui.help()

    def __list(self):
        self._cm.print_all()

    def __tag(self):
        if self._cm.add_tag_for_citation_by_user_input():
            self._tui.print("Tägi lisätty onnistuneesti")
        else:
            self._tui.print_error("Tägin lisäys ei onnistunut")

    def __add(self):
        if self._cm.add_citation_by_user_input():
            self._tui.print("Viite lisätty onnistuneesti")
        else:
            self._tui.print_error("Viitten lisäys ei onnistunut")

    def __drop(self):
        self._cm.clear_all()
        self._tui.print("Viitteet tyhjennetty")
#        else:
#            self._tui.print_error("Tyhjennys ei onnistunut")

    def __delete(self):
        self._cm.delete_citation()
        self._tui.print("Viite poistettu")
#        else:
#            self._tui.print_error("Viitteen poisto ei onnistunut")


if __name__ == "__main__":
    app = App()
    app.run()
