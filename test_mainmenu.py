from unicodedata import name
from AppDf import *

inputs = iter(["1", "name", "jaws", "back"])

def fake_input(prompt):
    return next(inputs)

class TestMainMenu():
    def test_menuoptions(self, monkeypatch):
        monkeypatch.setattr('builtins.input', fake_input)
        assert App_dataframe.show_main_menu() == "1"
     
 