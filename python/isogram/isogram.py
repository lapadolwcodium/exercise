def is_isogram(string):
    is_pass = False

    if not string:
        is_pass = True

    if string.islower():
        is_pass = True

    if "-" in string:
        is_pass = True

    center_string = string[1:-1]
    for cn in center_string:
        if center_string.count(cn) > 1:
            is_pass = False
            break

    duplicate_none = False
    duplicate_nor = False
    newString = string.lower()
    validNonLetters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for cc in newString:
        if cc not in validNonLetters:  #
            if newString.count(cc) > 1:
                is_pass = True
                duplicate_none = True
        else:
            if newString.count(cc) > 1:
                is_pass = False
                duplicate_nor = True

    if duplicate_nor and duplicate_none:
        is_pass = False

    return is_pass
