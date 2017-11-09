import re
from collections import Counter


def word_count(phrase):
    # g = re.split(r'[^a-zA-Z0-9]', phrase.lower())
    g = re.findall(r"[a-z0-9]+", phrase.lower())
    str_list = list(filter(None, g))
    countword = Counter(str_list)
    print(countword)
    return countword
