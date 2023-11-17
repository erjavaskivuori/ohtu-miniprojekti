from entities.citation import Citation
from tui.tui import Tui,Commands
from enum import Enum

tui = Tui()

while True:
    action = tui.menu()
    if action == Commands.QUIT:
        break
    if action == Commands.ADD:
        c = Citation(
                tui.ask("tyyppi"),
                tui.ask("tekijä"),
                tui.ask("otsikko"),
                tui.ask("vuosi",Citation.year_validator)
            )
    
    