""" app.py - The main application """

from logic.citation_manager import CitationManager
from citations.citation_strings import ATTR_TRANSLATIONS
from tui.tui import Tui, Commands
from tui.tui_io import TuiIO
from app_msg import MSG


class App:
    """ THE APPLICATION !!! """

    def __init__(self, io=TuiIO()):
        self._tui = Tui(io)
        self._cm = CitationManager()

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
                self._tui.print_error( MSG.not_implemented )
                break

    def __bib(self):
        filename = self._tui.ask( MSG.Bib.ask_filename )
        if self._cm.create_bib_file(filename):
            self._tui.print_info(MSG.Bib.create_ok)
        else:
            self._tui.print_error(MSG.Bib.create_fail)

    def __search(self):
        tag = self._tui.ask( MSG.Search.ask_tag )
        plist = self._cm.get_plist_by_tag(tag)
        self.__print_plist(plist)

    def __list(self):
        plist = self._cm.get_plist()
        self.__print_plist(plist)


    def __print_plist(self, plist):
        if len(plist) == 0:
            self._tui.print( MSG.List.empty )
        for (c_id, label), attrs in plist:
            self._tui.print_item_entry(c_id, label)
            for key, value in attrs:
                self._tui.print_item_attribute( key, value )



    def __tag(self):
        # Validator to be int
        def validate_int(x):
            try:
                int(x)
            except ValueError:
                return False
            return True

        if self._cm.return_all_citations() == {}:
            self._tui.print_error( MSG.Tag.fail_empty )
            return False

        self._tui.print( MSG.Tag.info_list )
        self.__list()

        citation_id = self._tui.ask( MSG.Tag.ask_for_id, validate_int )

        if not self._cm.citation_exists(citation_id):
            self._tui.print_error( MSG.Tag.fail_unknown )
            return False

        citations_tag = self._cm.tag_by_citation(citation_id)

        if citations_tag != [] and not self._tui.yesno(MSG.Tag.info_retag):
            return False

        if self._cm.get_all_tags() != {}:
            self._tui.print( MSG.Tag.info_taglist )
            self._tui.print("\n".join(self._cm.get_all_tags()))
            tag = self._tui.ask( MSG.Tag.ask_tag )
        else:
            tag = self._tui.ask( MSG.Tag.ask_new_tag )

        self._cm.add_tag_for_citation(citation_id, tag.lower())

        self._tui.print_info( MSG.Tag.success )
        return True


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
            label = self._tui.ask( MSG.Add.ask_label )
            if label == "\0":
                return False
            if self._cm.is_label_in_use(label):
                self._tui.print( MSG.Add.info_label_in_use )
                continue
            break

        # citation type
        try:
            ctype = int(self._tui.ask( MSG.Add.ask_type, validate_type ) )
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
        tag = self._tui.ask( MSG.Add.ask_tag ) \
                if self._tui.yesno( MSG.Add.ask_add_tag ) else ""

        self._cm.add_citation( ctype, label, tag, adict )
        self._tui.print_info( MSG.Add.success )
#        else:
#            self._tui.print_error( MSG.Add.fail )


    def __drop(self):
        if self._tui.yesno( MSG.Drop.ask_sure ):
            self._cm.clear_all()
            self._tui.print_info( MSG.Drop.success )
        else:
            self._tui.print( MSG.Drop.aborted )

    def __delete(self):
        citation_id = self._tui.ask( MSG.Delete.ask_id )
        try:
            citation_id = int(citation_id)
        except ValueError:
            self._tui.print_error( MSG.Delete.fail )
            return
        if self._cm.delete_citation(citation_id):
            self._tui.print_info( MSG.Delete.success )
        else:
            self._tui.print_error( MSG.Delete.fail )


if __name__ == "__main__":
    app = App()
    app.run()
