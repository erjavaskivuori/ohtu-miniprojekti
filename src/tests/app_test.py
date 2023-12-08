import unittest
import sys
from tui.tui import Commands, Tui
from tui.stub_io import StubIO
from tui.tui_io import TuiIO
from app import App
from app_msg import MSG
from db.initialize import initialize_database


class TestApp(unittest.TestCase):
    def setUp(self):
        initialize_database()
        self.io = StubIO()
        self.tui = Tui(self.io)
        self.app = App(self.tui)
        
    def add_citate1(self):
        self.io.add_input("lisää")
        self.io.add_input("label1")
        self.io.add_input("1")
        self.io.add_input("Test Book")
        self.io.add_input("Kake")
        self.io.add_input("202")
        self.io.add_input("kyllä")
        self.io.add_input("test_tag1")
    
        
    def test_app_starts(self):
        self.app.run()
        self.assertIn("TERVETULOA", "".join(self.io.outputs))
        
    def test_app_command_menu(self):
        self.io.add_input("menu")
        self.app.run()
        self.assertIn("Komennot:", "".join(self.io.outputs))
        
    def test_app_robot_exit(self):
        self.app._tui.menu = lambda: "\0"
        self.app.run()

    def test_app_menu_unimplemented(self):
        self.app._tui.menu = lambda: 666
        self.app.run()
        self.assertIn( MSG.not_implemented, "".join(self.io.outputs))

    def test_app_commands_list_empty(self):
        self.io.add_input("listaa")
        self.app.run()
        self.assertIn( MSG.List.empty , "".join(self.io.outputs))

    def test_app_commands_add_wrong_type(self):
        self.io.add_input("lisää")
        self.io.add_input("test")
        self.io.add_input("8")
        self.app.run()
        self.assertIn("Syöte '8' ei kelpaa.", "".join(self.io.outputs))

        self.io.outputs=[]
        self.io.add_input("lisää")
        self.io.add_input("test")
        self.io.add_input("muikku")
        self.app.run()
        self.assertIn("Syöte 'muikku' ei kelpaa.", "".join(self.io.outputs))

    def test_app_commands_add_wrong_year(self):
        self.io.add_input("lisää")
        self.io.add_input("test")
        self.io.add_input("1")
        self.io.add_input("testi_lisäys")
        self.io.add_input("test")
        self.io.add_input("3000")
        self.app.run()
        self.assertIn("Syöte '3000' ei kelpaa.", "".join(self.io.outputs))

        self.io.outputs=[]
        self.io.add_input("lisää")
        self.io.add_input("test")
        self.io.add_input("1")
        self.io.add_input("testi_lisäys")
        self.io.add_input("test")
        self.io.add_input("kissa")
        self.app.run()
        self.assertIn("Syöte 'kissa' ei kelpaa.", "".join(self.io.outputs))
        
    def test_app_add_with_tag(self):
        self.io.add_input("lisää")
        self.io.add_input("test")
        self.io.add_input("1")
        self.io.add_input("testi_lisäys")
        self.io.add_input("test")
        self.io.add_input("2004")
        self.io.add_input("kyllä")
        self.io.add_input("tag")
        self.app.run()
        self.assertIn( MSG.Add.ask_tag, "".join(self.io.outputs))
    

    def test_app_commands_drop_add_list_tag_search_delete(self):
        self.io.add_input("tyhjennä")
        self.io.add_input("kyllä")
        self.app.run()
        self.assertIn( MSG.Drop.success, "".join(self.io.outputs))
    
        self.io.outputs=[]
        self.io.add_input("tyhjennä")
        self.io.add_input("ei")
        self.app.run()
        self.assertIn( MSG.Drop.aborted, "".join(self.io.outputs))
    
        self.io.add_input("lisää")
        self.app.run()
        self.assertNotIn( MSG.Add.success, "".join(self.io.outputs))
        
        self.io.outputs=[]
        self.io.add_input("lisää")
        self.io.add_input("test")
        self.io.add_input("1")
        self.io.add_input("testi_lisäys")
        self.io.add_input("test")
        self.io.add_input("2004")
        self.io.add_input("ei")
        self.app.run()
        self.assertIn( MSG.Add.success, "".join(self.io.outputs))

        self.io.outputs=[]
        self.io.add_input("listaa")
        self.app.run()
        self.assertIn("testi_lisäys", "".join(self.io.outputs))
        
        self.io.outputs=[]
        self.io.add_input("tägää")
        self.io.add_input("1")
        self.io.add_input("testi_tägi666")
        self.app.run()
        self.assertIn( MSG.Tag.success, "".join(self.io.outputs))
        
        self.io.outputs=[]
        self.io.add_input("tägää")
        self.io.add_input("666")
        self.io.add_input("testi_tägi666")
        self.app.run()
        self.assertIn( MSG.Tag.fail_unknown, "".join(self.io.outputs))
        
        self.io.outputs=[]
        self.io.add_input("hae")
        self.io.add_input("testi_tägi666")
        self.app.run()
        self.assertIn("testi_lisäys", "".join(self.io.outputs))
        
        self.io.outputs=[]
        self.io.add_input("hae")
        self.io.add_input("etlöydy")
        self.app.run()
        self.assertIn("Viitteitä ei löydy.", "".join(self.io.outputs))
        
        self.io.outputs=[]
        self.io.add_input("luo")
        self.io.add_input("unittest")
        self.app.run()
        self.assertIn( MSG.Bib.create_ok , "".join(self.io.outputs))

        self.io.outputs=[]
        self.io.add_input("luo")
        self.io.add_input("?#<2")
        self.app.run()
        self.assertIn( MSG.Bib.create_fail, "".join(self.io.outputs))

        
        self.io.outputs=[]
        self.io.add_input("poista")
        self.io.add_input("1")
        self.app.run()
        self.assertIn( MSG.Delete.success, "".join(self.io.outputs))
        
#        self.io.outputs=[]
#        self.io.add_input("poista")
#        self.io.add_input("666")
#        self.app.run()
#        self.assertIn( MSG.Delete.fail , "".join(self.io.outputs))


        self.io.add_input("lopeta")
        self.app.run()
        
    def test_app_tagging_fails_on_empty_list(self):
        self.io.add_input("tägää")
        self.app.run()
        self.assertIn( MSG.Tag.fail_empty, "".join(self.io.outputs))

    def test_app_tag_list_gets_printed(self):
        self.add_citate1()
        self.io.add_input("tägää")
        self.io.add_input("1")
        self.app.run()
        self.assertIn( "test_tag1", "".join(self.io.outputs))


        