#pylint: disable=w0613
class StubIO:
    def __init__(self, inputs=None):
        self.inputs = inputs or []
        self.outputs = []

    def output(self, value):
        self.outputs.append(str(value))

    def input(self):
        if len(self.inputs) > 0:
            return self.inputs.pop(0)
        # If list of inputs is empry, give \0 as input continously
        return "\0"

    def add_input(self, value):
        self.inputs.append(value)
