
def fasta_to_one_line(seq):
    header_end_at = seq.find('\n')
    seq = seq[header_end_at + 1:]
    seq = seq.replace('\n', '')
    return seq

