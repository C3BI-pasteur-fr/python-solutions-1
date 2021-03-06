
def get_kmer_occurences(seq, kmer_len):
    """
    return a list of tuple 
    each tuple contains a kmers present in seq and its occurence
    """
    kmers = {}
    stop = len(seq) - kmer_len
    for i in range(stop + 1):
        kmer = s[i : i + kmer_len]
        kmers[kmer] = kmers.get(kmer, 0) + 1
    return kmers.items()