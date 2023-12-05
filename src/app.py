""" app.py - The main application """

from logic.citation_manager import CitationManager
from citations.citation_strings import ATTR_TRANSLATIONS
from tui.tui import Tui, Commands
from tui.tui_io import TuiIO


# Näin että stringit aina mätsäävät eikä kirjoitusvirhe
# esimerkiksi failaa testejä
class MSG:
    class Bib:
        create_ok = "Tiedosto luotu onnistuneesti"
        create_fail = "Tiedoston luonti epäonnistui \
(tarkista oikeudet tai käytitkö kiellettyjä merkkejä)"



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
        filename = self._tui.ask("tiedoston nimi (.bib)")
        if self._cm.create_bib_file(filename):
            self._tui.print(MSG.Bib.create_ok)
        else:
            self._tui.print(MSG.Bib.create_fail)

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
        """ Asks all the nessessary information to make citation and calls cm
        """
        # Validator for type
        def validate_type(x):
            try:
                return int(x) > 0 and int(x) < 4
            except ValueError:
                pass
            return False

        # Validator for year
        def validate_year(x):
            try:
                return int(x) > 0 and int(x) < 2030
            except ValueError:
                pass
            return False

        # citation label
        while True:
            label = self._tui.ask("tunniste")
            if label == "\0":
                return False
#            if self._cm.is_label_in_use(label):
#                self._tui.print_error("Tunniste on jo käytössä")
#                continue
            break

        # citation type
        try:
            ctype = int(self._tui.ask( "tyypin numero, vaihtoehtoja ovat \
Kirja (1), Artikkeli (2) ja Inproceedings (3)", validate_type ) )
        except ValueError:
            return False

        # other attributes
        attrs = self._cm.get_attrs_by_ctype(ctype)
        adict={}
        for attr in attrs:
            adict[attr] = self._tui.ask(
                f"{ATTR_TRANSLATIONS[attr]} ({attr})",
                validate_year if attr == "year" else lambda x: True
            )

        # add the tag
        tag = self._tui.ask("tägi") \
                if self._tui.yesno("Lisätäänkö tägi (kyllä/ei):") else ""

        self._cm.add_citation( ctype, label, tag, adict )
        self._tui.print("Viite lisätty onnistuneesti")
#        else:
#            self._tui.print_error("Viitten lisäys ei onnistunut")


    def __drop(self):
        if self._tui.yesno("Oletko ihan varma (kyllä/ei):"):
            self._cm.clear_all()
            self._tui.print("Viitteet tyhjennetty")
        else:
            self._tui.print("Tyhjennys peruutettu.")

    def __delete(self):
        citation_id = self._tui.ask("sitaatin id")
        self._cm.delete_citation(citation_id)
        self._tui.print("Viite poistettu")
#        else:
#            self._tui.print_error("Viitteen poisto ei onnistunut")


if __name__ == "__main__":
    app = App()
    app.run()
