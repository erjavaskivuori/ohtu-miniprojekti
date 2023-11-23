#pylint: disable=w0613
class StubIO:
    def __init__(self, inputs=None):
        self.inputs = inputs or []
        self.outputs = []

    def output(self, value):
        #print(f"We are in StubIO.output(). Appending to output list:{value}")
        self.outputs.append(value)
        #print("arvot ovat:", self.outputs)

    def input(self, prompt):
        if len(self.inputs) > 0:
            #print("We are in StubIO.input()")
            return self.inputs.pop(0)
        #return ""
        raise RuntimeError("No input given")

    def add_input(self, value):
        self.inputs.append(value)
