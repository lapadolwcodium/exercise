from functional import seq


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

    is_dup_none = False
    is_dup_char = False

    new_string_lower = string.lower()
    char_list = list(new_string_lower)
    valid_non_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    dup_char = seq(char_list) \
        .where(lambda x: new_string_lower.count(x) > 1) \
        .select(lambda s: s) \
        .distinct() \
        .to_list()

    if len(dup_char) > 0:
        char_dup_char = list(dup_char)
        is_dup_char = seq(char_dup_char) \
            .where(lambda x: x in valid_non_letters) \
            .any()

        is_pass = is_dup_none = seq(char_dup_char) \
            .where(lambda x: x not in valid_non_letters) \
            .any()
 
    if is_dup_char and is_dup_none:
        is_pass = False

    return is_pass
