import string
# string est une librairie intégrée à python

from ..modules import solenne as ms

def parse_punctuation(text):
    """Cette fonction retire la ponctuation d'une phrase

    Args:
        text (str): Texte contenant de la ponctuation

    Returns:
        str: Texte sans ponctuation
    """
    return "".join(
        [
            char for char in text if char not in string.punctuation
        ]
    ).strip()


def parse_text(text):
    """Cette fonction supprime la ponctuation et les stop-words
    d'un texte

    Args:
        text (str): texte non parsé

    Returns:
        str: texte entièrement parsé :)
    """
    return parse_punctuation(ms.parse_stop_words(text))