from unicodedata import name
from AppDf import *

inputs = iter(["4", "start", "hint", "jaws", "yes"])

def fake_input(prompt):
    return next(inputs)

class TestMainMenu():
    def test_menuoptions(self, monkeypatch):
        monkeypatch.setattr('builtins.input', fake_input)
        assert App_dataframe.show_main_menu() == "start"
     
#Tests fail due to exhaustion of inputs
#Note: since these functions are built as infinite loops, they were tested based on each iteration and therefore will break unless infinite iterations are provided
