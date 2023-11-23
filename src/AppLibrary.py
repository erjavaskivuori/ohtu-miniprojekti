# pylint: disable=C0103
from tui.stub_io import StubIO
from app import App


class AppLibrary:
    def __init__(self):
        self._io = StubIO()
        self._app = App(self._io)

    def input(self, value):
        self._io.add_input(value)

    def output_should_contain(self, value):
        print("We are in AppLibrary.output_should_contain()")
        outputs = self._io.outputs

        if not value in outputs:
            raise AssertionError(
                f"Output \"{value}\" is not in {str(outputs)}"
            )

    def run_application(self):
        self._app.run()
