from ..modules import emmanuelle as em 


class MockResponse():
    @staticmethod
    def json():
        return [{"mock": "fake"}]

def mock_request(mock1):
    return MockResponse()


def test_wiki_request_place_story(monkeypatch):
    monkeypatch.setattr("requests.get", mock_request)
    result = em.wiki_request_place_story("Paris")
    assert result == [{"mock": "fake"}]

def mock_wiki_request_place_story(mock2):
    return {"query": {"pages": {"123": {"extract" : "valeur qu'on recherche"}}}}

def test_request_place_storydata(monkeypatch):
    monkeypatch.setattr(em, "wiki_request_place_story", mock_wiki_request_place_story)
    assert em.request_place_storydata("ee") == "valeur qu'on recherche"


# integration test

def test_integration():
    result = em.request_place_storydata("tokyo")
    assert "la capitale actuelle du Japon" in result