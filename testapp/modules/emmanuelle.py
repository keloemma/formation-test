import requests
from ..modules import jonas as mjo


def wiki_request_place_story(place):
    url = [
        "https://fr.wikipedia.org/w/api.php?format=json",
        "&action=query&prop=extracts&exintro&explaintext&redirects=1&titles=",
        place,
    ]
    request = requests.get("".join(url))
    return request.json()


def request_place_storydata(place):
    """Cette fonction lance la fonction wiki_request puis renvoie les données

    Args:
        parsed_text (str): Nom d'un lieu

    Returns:
        str: Détails sur le lieu et son histoire
    """
    try:
        json = wiki_request_place_story(place)
        for key in json["query"]["pages"]:
            story = json["query"]["pages"][key]["extract"]
            break
    except:
        story = mjo.return_fail_sentence()
    return story
