from testapp.data import FAIL_SENTENCE
from ..modules import jonas as jn
from .. import data as dt

def mock_even(a, b):
    return 2

def mock_odd(a, b):
    return 1

def mock_0(a, b):
    return 0

def test_odd_or_even0(monkeypatch):
    monkeypatch.setattr("random.randint", mock_even)
    assert jn.odd_or_even() == "even"

def test_odd_or_even1(monkeypatch):
    monkeypatch.setattr("random.randint", mock_odd)
    assert jn.odd_or_even() == "odd"

def test_odd_or_even2(monkeypatch):
    monkeypatch.setattr("random.randint", mock_0)
    assert jn.odd_or_even() == "even"

mock_FAIL_SENTENCE = {
    "odd": "Je n'ai rien trouvé !",
    "even": "Hum... je ne vois pas..."
}

def test_return_fail_odd0(monkeypatch):
    monkeypatch.setattr(dt, "FAIL_SENTENCE", mock_FAIL_SENTENCE)
    monkeypatch.setattr("random.randint", mock_odd)
    assert jn.return_fail_sentence() == "Je n'ai rien trouvé !"

def test_return_fail_odd1(monkeypatch):
    monkeypatch.setattr(dt, "FAIL_SENTENCE", mock_FAIL_SENTENCE)
    monkeypatch.setattr("random.randint", mock_even)
    assert jn.return_fail_sentence() == "Hum... je ne vois pas..."

def test_return_fail_odd_full():
    rs = ["Je n'ai rien trouvé !",
          "Hum... je ne vois pas..."]
    r_fn = []
    for i in range(1000):
        r_fn.append(jn.return_fail_sentence())
    for r in rs:
        assert r in rs