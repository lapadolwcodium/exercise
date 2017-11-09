from collections import Iterable


def is_contain(out):
    return isinstance(out, Iterable) and not isinstance(out, str)


def flatten(iterable):
    result = []
    for ech_ar in iterable:
        if is_contain(ech_ar):
            result.extend(flatten(ech_ar))
        elif ech_ar is not None:
            result.append(ech_ar)
    return result
