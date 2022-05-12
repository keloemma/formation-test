import stop_words

from ..modules import jerome as mj


def parse_stop_words(text):
    """Cette fonction retire certains mots d'une phrase

    Args:
        text (str): Texte contenant des mots interdits

    Returns:
        str: Texte sans mots interdits
    """
    return " ".join(
        [
            word for word in text.split() if word not in stop_words.get_stop_words("french")
        ]
    )


def parse_text(text):
    """Cette fonction supprime la ponctuation et les stop-words
    d'un texte

    Args:
        text (str): texte non parsé

    Returns:
        str: texte entièrement parsé :)
    """
    return parse_stop_words(mj.parse_punctuation(text))
