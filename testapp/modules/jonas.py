import random

from .. import data as dt


def odd_or_even():
    """Cette fonction renvoi "pair" ou "impair" de façon aléatoire

    Returns:
        str: paire (even) ou impair (odd)"
    """
    return "even" if random.randint(1, 2) % 2 == 0 else "odd"


def return_fail_sentence():
    """Cette fonction renvoi une phrase choisie au hasard
    si la recherche de lieu est un échec

    Returns:
        str: phrase d'échec
    """
    return dt.FAIL_SENTENCE[odd_or_even()]