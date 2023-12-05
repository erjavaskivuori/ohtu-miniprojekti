# pylint: disable=C0103
from tui.stub_io import StubIO
from app import App


class AppLibrary:
    def __init__(self):
        self._io = StubIO()
        self._app = App(self._io)

    def input(self, value):
        self._io.add_input(value)

    def output_should_contain_line(self, value):
        if not value in self._io.outputs:
            out = "\n".join(self._io.outputs)
            raise AssertionError( f"\"{value}\" is not a line in:\n\n{out}" )

    def output_should_contain(self, value):
        if value not in "".join(self._io.outputs):
            out = "\n".join(self._io.outputs)
            raise AssertionError( f"\"{value}\" is found in:\n\n{out}" )

    def output_should_not_contain(self, value):
        if value in "".join(self._io.outputs):
            out = "\n".join(self._io.outputs)
            raise AssertionError( f"\"{value}\" is not found in:\n\n{out}" )


    def reset_database(self):
# pylint: disable=W0212
        self._app._cm.clear_all()


    def run_application(self):
        self._app.run()
