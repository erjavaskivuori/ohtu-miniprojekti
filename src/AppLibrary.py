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
        print("We are in AppLibrary.output_should_contain()")
        outputs = self._io.outputs

        if not value in outputs:
            raise AssertionError(
                f"Output \"{value}\" is not line in {str(outputs)}"
            )

    def output_should_contain(self, value):
        print("We are in AppLibrary.output_should_contain()")
        outputs = self._io.outputs
        found = [line for line in outputs if line.find(value) > 0]

        if not found:
            raise AssertionError(
                f"String \"{value}\" is not found in {str(outputs)}"
            )

    def output_should_not_contain(self, value):
        print("We are in AppLibrary.output_should_contain()")
        outputs = self._io.outputs
        found = [line for line in outputs if line.find(value) > 0]

        if found:
            raise AssertionError(
                f"String \"{value}\" is found in {str(outputs)}"
            )

    def reset_database(self):
        # pylint: disable=W0212
        self._app._cm.clear_all()

    def run_application(self):
        self._app.run()
