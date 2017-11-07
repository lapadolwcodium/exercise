from collections import Counter
import re

def word_count(phrase):
    #g = re.split(r'[^a-zA-Z0-9]', phrase.lower())
    g = re.split(r'[^a-z0-9]', phrase.lower())
    str_list = list(filter(None, g))
    countword = Counter(str_list)
    print(countword)
    return countword