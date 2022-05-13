"""TEST DORIANE"""
from ..modules import doriane as md

# UNITAIRE
class MockResponse():
    @staticmethod
    def json():
        return [{"mock": "fake"}]


def mock_request(mock1):
    return MockResponse()


def test_osm_request(monkeypatch):
    monkeypatch.setattr("requests.get", mock_request)
    result = md.osm_request("tour eiffel")
    assert result == [{"mock": "fake"}]


def mock_osm_request(mock1):
    return [{
        "lat": 1,
        "lon": 2,
    }]


def test_request_place_geodata(monkeypatch):
    monkeypatch.setattr(md, "osm_request", mock_osm_request)
    result = md.request_place_geodata("truc")
    assert result == {
        "lat": 1,
        "lon": 2,
    }

# INTEGRATION
def test_place_research_return_result():
    result = md.request_place_geodata("tour eiffel")
    assert result == {
        'lat': '48.858260200000004',
        'lon': '2.2944990543196795'
    }
    
    

"""TEST SOLENNE"""
from ..modules import solenne as ms
from ..modules import jerome as mje

# UNITAIRE
def mock_stop_words(mock1):
    return ["tu", "es", "est", "un"]


def mock_punctuation(mock1):
    return "Hey tu es un analyste"


def test_parse_stop_words(monkeypatch):
    monkeypatch.setattr("stop_words.get_stop_words", mock_stop_words)
    result = ms.parse_stop_words("ceci est un test")
    assert result == "ceci test"


def test_parse_text_solenne(monkeypatch):
    monkeypatch.setattr("stop_words.get_stop_words", mock_stop_words)
    monkeypatch.setattr(mje, "parse_punctuation", mock_punctuation)
    text = "Hey! tu es un analyste ?"
    result = ms.parse_text(text)
    assert result == "Hey analyste"

# INTEGRATION
def test_parse_text_solenne_integration():
    text = "Hey! tu es un analyste ?"
    result = ms.parse_text(text)
    assert result == "Hey analyste"


"""TEST JONAS"""
from ..modules import jonas as mj
from .. import data as dt

# UNITAIRE
def mock_random(mock1, mock2):
    return 2


def mock_odd_or_even():
    return "key"


def test_odd_or_even(monkeypatch):
    monkeypatch.setattr("random.randint", mock_random)
    result = mj.odd_or_even()
    assert result == "even"


def test_return_fail_sentence(monkeypatch):
    monkeypatch.setattr(mj, "odd_or_even", mock_odd_or_even)
    monkeypatch.setattr(dt, "FAIL_SENTENCE", {"key": "value"})
    result = mj.return_fail_sentence()
    assert result == "value"

# INTEGRATION
def mock_random_again(mock1, mock2):
    return 2

def test_fail_research(monkeypatch):
    monkeypatch.setattr("random.randint", mock_random_again)
    result = mj.return_fail_sentence()
    assert result == "Hum... je ne vois pas..."


"""TEST EMMANUELLE"""
from ..modules import emmanuelle as me


# UNITAIRE
class MockResponseWiki():
    @staticmethod
    def json():
        return {"mock": "fake"}


def mock_request_wiki(mock1):
    return MockResponseWiki()


def test_wiki_request(monkeypatch):
    monkeypatch.setattr("requests.get", mock_request_wiki)
    result = me.wiki_request_place_story("tour eiffel")
    assert result == {"mock": "fake"}


def mock_wiki_request(mock1):
    return {
        "query": {
            "pages": {
                "12345": {
                    "extract": "c'est l'histoire de la vie. Le cycle éternel !"
                },
                "67890": {
                    "extract": "rien"
                }
            }
        }
    }


def test_request_place_storydata(monkeypatch):
    monkeypatch.setattr(me, "wiki_request_place_story", mock_wiki_request)
    result = me.request_place_storydata("truc")
    assert result == "c'est l'histoire de la vie. Le cycle éternel !"


# INTEGRATION
def test_request_place_storydata_integration():
    result = me.request_place_storydata("Tour Eiffel")
    assert "La tour Eiffel  est une tour de fer puddlé de 330 mètres" in result


"""TEST JERÔME"""
# from ..modules import jerome as mje
# from ..modules import solenne as ms


def test_parse_punctuation():
    text = "Hello, tout va bien ???"
    result = mje.parse_punctuation(text)
    assert result == "Hello tout va bien"


def mock_parse_stop_words(mock1):
    return "Salut, comment?"


def test_parse_text_jerome(monkeypatch):
    monkeypatch.setattr(ms, "parse_stop_words", mock_parse_stop_words)
    text = "Salut, comment ça va ?"
    result = mje.parse_text(text)
    assert result == "Salut comment"


# INTEGRATION
def test_parse_text_jerome_integration():
    text = "Hey! tu es un analyste ?"
    result = ms.parse_text(text)
    assert result == "Hey analyste"
