class TuiIO:
    def output(self, value):
        print(value, end="")

    def input(self, prompt):
        return input(prompt)
