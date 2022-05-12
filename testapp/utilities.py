import requests

def wiki_request_place_name(place):
    """Cette fonction passe une requête GET à wikipedia et renvoi un json

    Args:
        parsed_text (str): Nom d'un lieu

    Returns:
        json: Json contenant les datas du lieu recherché
    """
    url = [
        "https://fr.wikipedia.org/w/api.php?action=query&list=search&srsearch=",
        place,
        "&format=json",
    ]
    # tip 1 : request est un objet de classe
    request = requests.get("".join(url))
    # tip 2 : json() est une méthode statique de la classe créée par requests
    return request.json()["query"]["search"][0]["title"]