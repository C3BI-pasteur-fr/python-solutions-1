
def amplicon_len(seq, primer_1, primer_2):
    """
    given primer_1 and primer_2 
    return the lenght of the amplicon
    primer_1 and primer_2 ar present and in this order 
    in sequence 
    """
    primer_1 = primer_1.upper()
    primer_2 = primer_2.upper()
    sequence = sequence.upper()
    pos_1 = sv40_sequence.find(primer_1)
    pos_2 = sv40_sequence.find(primer_2)
    amplicon_len = pos_2 + len(primer_2) - pos_1
    return amplicon_len