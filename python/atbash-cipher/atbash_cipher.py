def mapper_encode(chr_a):
    if chr_a.isdigit():
        return chr_a
    if chr_a.islower():
        ths_ord = ord(chr_a)
        a_ord = ord('a')
        z_ord = ord('z')
        if ths_ord <= a_ord + 12:
            chr_a = chr(z_ord - (ths_ord - a_ord))
        else:
            chr_a = chr(a_ord + (z_ord - ths_ord))
        return chr_a
    return ''


def encode(plain_text):
    text_lower = plain_text.lower()
    e_map = ''.join(map(lambda x: mapper_encode(x), text_lower))
    j_5space = ' '.join([e_map[i:i + 5] for i in range(0, len(e_map), 5)])
    # print(plain_text, j_5space)
    return j_5space


def decode(ciphered_text):
    ciphered_text = ciphered_text.strip()
    e_map = ''.join(map(lambda x: mapper_encode(x), ciphered_text))
    # print(ciphered_text, e_map)
    return e_map
