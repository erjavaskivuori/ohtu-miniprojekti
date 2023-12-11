import sqlite3
import unittest
import sys
import os
from tui.tui import Commands, Tui
from tui.stub_io import StubIO
from tui.tui_io import TuiIO
from app import App
from app_msg import MSG
from db.initialize import initialize_database
from db.populate import populate_citations_from_file
from config import DATABASE_FILE_PATH, POPULATE_CITATIONS_PATH


class TestPopDB(unittest.TestCase):
    def test_list_popupated(self):
        initialize_database()
        conn = sqlite3.connect(DATABASE_FILE_PATH)
        populate_citations_from_file(conn, POPULATE_CITATIONS_PATH)
        conn.close()
        self.io = StubIO()
        self.tui = Tui(self.io)
        self.app = App(self.tui)
        self.io.add_input("listaa")
        self.app.run()
        self.assertNotIn( MSG.List.empty , "".join(self.io.outputs))
        
