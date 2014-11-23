import string

def rev_comp(seq):
    """
    return the reverse complement of seq
    the case is respect but if the sequence mix upper and lower case the function will failed
    """
    upper = seq.isupper()
    reverse = seq[::-1]
    direct = 'acgt'
    comp = 'tgca'
    if upper:
        table = string.maketrans(direct.upper(), comp.upper())
    else:
        table = string.maketrans(direct, comp)
    rev_comp = reverse.translate(table)
    return rev_comp