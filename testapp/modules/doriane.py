import requests


def osm_request(parsed_text):
    """Cette fonction passe une requête GET à OpenStreetMap et renvoi un json

    Args:
        parsed_text (str): Texte parsé contenant un lieu à trouver

    Returns:
        json: Json contenant les datas de l'endroit recherché
    """
    # requests n'aime pas du tout les f-strings ;)
    url = [
        "https://nominatim.openstreetmap.org/search/",
        parsed_text,
        "?format=json&addressdetails=1",
        "&limit=1",
        "&accept-language=fr",
    ]
    # tip 1 : request est un objet de classe
    request = requests.get("".join(url))
    # tip 2 : json() est une méthode statique de la classe créée par requests
    return request.json()


def request_place_geodata(parsed_text):
    """Cette fonction lance la fonction osm_request puis renvoie les données

    Args:
        parsed_text (str): Texte parsé contenant un lieu à trouver

    Returns:
        dict: Dictionnaire contenant les infos essentielles à l'application
    """
    json = osm_request(parsed_text)
    return {
        "lat": json[0]["lat"],
        "lon": json[0]["lon"],
    } if len(json) > 0 else {
        "lat": 0,
        "lon": 0,
    }
