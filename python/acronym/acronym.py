import re


def abbreviate(words):
    re_special = re.findall(r"[\w']+", words)
    # print(re_special)

    first_char = map(lambda ss: ss[0:1], re_special)
    # print(first_char)

    str_connect = ''.join(first_char).upper()
    # print(str_connect)
    return str_connect
