import re


def hey(phrase : string):
    if phrase.isupper():
        return "Whoa, chill out!"

    if phrase.replace(" ", "").endswith('?'):
        return "Sure."

    if re.search('[\w]+', phrase):
        return "Whatever."

    return "Fine. Be that way!"
