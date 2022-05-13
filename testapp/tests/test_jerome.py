from ..modules import jerome as jfile
from ..modules import solenne as sfile

def test_pp():
    assert jfile.parse_punctuation("mon,;: exemple") == "mon exemple"

def mock_pp(blabla):
    return ('mon exemple')

def mock_psw(blablabla):
    return (',,;;')

def test_pt(monkeypatch):
    monkeypatch.setattr(jfile, "parse_punctuation", mock_pp)
    monkeypatch.setattr(sfile, "parse_stop_words", mock_psw)
    assert jfile.parse_text('mon, exemple exemple') == 'mon exemple'

def test_inte():
    assert jfile.parse_text("mon, test; est: bon bonjour je coucou ") == "mon test est bonjour coucou"

