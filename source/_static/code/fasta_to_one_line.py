
def fasta_2_one_line(seq):
    header_end_at = find('\n')
    seq = seq[:header_end_at + 1]
    seq = seq.replace('\n', '')
    return seq

