import unittest
import sys
from tui.tui import Commands, Tui
from tui.stub_io import StubIO
from tui.tui_io import TuiIO


class TestTui(unittest.TestCase):
    def setUp(self):
        self.io = StubIO()
        self.tui = Tui(self.io)
        
    def test_function_greet(self):
        self.tui.greet()
        self.assertIn("TERVETULOA", self.io.outputs[-1])

    def test_function_print(self):
        self.tui.print("testing printing")
        self.assertIn("testing printing", self.io.outputs[-1])

    def test_function_print_error(self):
        self.tui.print_error("testing error")
        self.assertIn("VIRHE: testing error", self.io.outputs[-1])

    def test_function_help(self):
        self.tui.help()
        self.assertIn("valikossa syötetään toiminto", "".join(self.io.outputs))
        self.assertIn("BiBTeX muodossa", "".join(self.io.outputs))
        
    def test_function_ask_without_input(self):
        ret_val = self.tui.ask("moi")
        self.assertIn("Syötä moi:", self.io.outputs[-1])
        self.assertEqual(ret_val, "\0")
        
    def test_function_ask_input(self):
        self.io.add_input("kookoo")
        ret_val = self.tui.ask("moi")
        self.assertEqual(ret_val, "kookoo")
        
    def test_function_ask_validator(self):
        self.io.add_input("kookos")
        ret_val = self.tui.ask("moi", lambda a: False)
        self.assertIn("'kookos' ei kelpaa.", "".join(self.io.outputs))
        self.assertEqual(ret_val, "\0")
        
    def test_function_yesno_without_input(self):
        ret_val = self.tui.yesno("Kyllei")
        self.assertIn("Kyllei:", self.io.outputs[-1])
        self.assertEqual(ret_val, False)
        
    def test_function_yesno_with_no(self):
        self.io.add_input("ei")
        ret_val = self.tui.yesno("")
        self.assertEqual(ret_val, False)
        
    def test_function_yesno_with_invalid_and_then_yes(self):
        self.io.add_input("haloo")
        self.io.add_input("joo")
        ret_val = self.tui.yesno("")
        self.assertIn("'haloo' ei kelpaa.", "".join(self.io.outputs))
        self.assertEqual(ret_val, True)
        
    def test_function_print_item_entry(self):
        self.tui.print_item_entry("cite_id666", "label666")
        self.assertIn("cite_id666", "".join(self.io.outputs))
        self.assertIn("label666", "".join(self.io.outputs))

    def test_function_print_item_attribute(self):
        self.tui.print_item_attribute("atribute666","value666")
        self.assertIn("atribute666", "".join(self.io.outputs))
        self.assertIn("value666", "".join(self.io.outputs))

    def test_fuction_menu_prompt_and_test_exit(self):
        ret_val = self.tui.menu()
        self.assertEqual(ret_val, "\0")
        self.assertIn("Komento (apu: syötä menu):", "".join(self.io.outputs))

    def test_fuction_menu_invalid_menu_entry(self):
        self.io.add_input("haloo")
        self.tui.menu()
        self.assertIn("haloo: tuntematon komento.", "".join(self.io.outputs))

    def test_fuction_menu_valid_menu_entry(self):
        self.io.add_input("apua")
        ret_val = self.tui.menu()
        self.assertEqual(ret_val, Commands.HELP)

    def test_fuction_menu_EOFError(self):
        def input_EOFError():
            raise EOFError
        self.tui.input = input_EOFError
        ret_val = self.tui.menu()
        self.assertEqual(ret_val, "\0")

    def test_fuction_menu_KeyboardInterrupt(self):
        def input_KeyboardInterrupt():
            global ki_case
            try:
                ki_case
            except NameError:
                ki_case = True
                raise KeyboardInterrupt
            return "\0"
        self.tui.input = input_KeyboardInterrupt
        ret_val = self.tui.menu()
        self.assertEqual(ret_val, "\0")

class TestTuiIO(unittest.TestCase):
    def setUp(self):
        self.io = TuiIO()
    
    def test_fuction_output(self):
        self.io.output("test")
        
    def test_fuction_input(self):
        sys.stdin = open("README.md")
        self.io.input()
        