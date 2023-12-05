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
            Commands.HELP:		self._tui.help,
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
        tag = self._tui.ask("tägi")
        plist = self._cm.get_plist_by_tag(tag)
        self.__print_plist(plist)

    def __list(self):
        plist = self._cm.get_plist()
        self.__print_plist(plist)

    def __print_plist(self, plist):
        if len(plist) == 0:
            self._tui.print("Viitteitä ei löydy.")
        for (c_id, label), attrs in plist:
            self._tui.print_item_entry(c_id, label)
            for key, value in attrs:
                self._tui.print_item_attribute( key, value )

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
