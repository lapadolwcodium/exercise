def distance(strand_a, strand_b):
    count = \
        sum( \
            int(char_strand_a != char_strand_b) \
            for char_strand_a, char_strand_b in \
            zip(strand_a, strand_b))
    # print (count)
    return count
