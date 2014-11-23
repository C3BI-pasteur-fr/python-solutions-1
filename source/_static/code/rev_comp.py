
def rev_comp(seq):
    """
    return the reverse complement of seq
    the sequence must be in lower case
    """
    complement = {'a' : 't',
                  'c' : 'g',
                  'g' : 'c',
                  't' : 'a'}
    rev_seq = seq[::-1]
    rev_comp = ''
    for nt in rev_seq:
        rev_comp += complement[nt]
    return rev_comp