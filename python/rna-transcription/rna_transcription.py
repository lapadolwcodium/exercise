from functional import seq


def parse_each_char(chr):
    if chr == 'G':
        return 'C'
    if chr == 'C':
        return 'G'
    if chr == 'T':
        return 'A'
    if chr == 'A':
        return 'U'


def to_rna(dna_strand):
    chr_dna = list(dna_strand)
    valid_dna = "GCTA"

    is_invalid = seq(chr_dna) \
        .where(lambda x: x not in valid_dna) \
        .any()

    if is_invalid:
        return ''

    map_dna = seq(chr_dna) \
        .map(lambda x: parse_each_char(x))

    # print (''.join(chr_dna), ''.join(map_dna))
    return ''.join(map_dna)
