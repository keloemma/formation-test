from ..modules import solenne as ms
from ..modules import jerome as mj

#Tests unitaires 
def mock_get_stop_words(french):
    return ["Cette","nous"]

def mock_parse_stop_words(text):
    return "après midi participons à un atelier sur les tests"

def mock_parse_punctuation(text):
    return "Cette après midi nous participons à un atelier sur les tests"

def test_parse_stop_words(monkeypatch):
    monkeypatch.setattr("stop_words.get_stop_words",mock_get_stop_words)
    resultat = ms.parse_stop_words("Cette après midi, nous participons à un atelier sur les tests.")
    assert resultat == "après midi, participons à un atelier sur les tests."

def test_parse_text(monkeypatch):
    monkeypatch.setattr(mj,"parse_punctuation",mock_parse_punctuation)
    monkeypatch.setattr(ms,"parse_stop_words",mock_parse_stop_words)
    resultat = ms.parse_text("Cette après midi, nous participons à un atelier sur les tests.")
    assert resultat == "après midi participons à un atelier sur les tests"

#Tests d'intégrations 
def test_integration():
    assert ms.parse_text("Cette après midi, nous participons à un atelier sur les tests.") == "Cette après midi participons atelier tests"