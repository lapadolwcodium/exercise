from functional import seq


def mapper(x, key):
    c = chr(ord(x) + key)
    if x.islower():
        if c.islower():
            return c
        else:
            c = chr(ord(x) + key - 26)
            return c
    if x.isupper():
        if c.isupper():
            return c
        else:
            c = chr(ord(x) + key - 26)
            return c

    return x


def rotate(text, key):
    map_rotate = seq(list(text)) \
        .map(lambda x: mapper(x, key))

    return ''.join(map_rotate)
