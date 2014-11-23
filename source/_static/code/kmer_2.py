import collections
from operator import itemgetter

def get_kmer_occurences(seq, kmer_len):
    """
    return a list of tuple 
    each tuple contains a kmers present in seq and its occurence
    """
    kmers = collections.defaultdict(int)
    stop = len(seq) - kmer_len
    for i in range(stop + 1):
        kmer = s[i : i + kmer_len]
        kmers[kmer] += 1
    kmers = kmers.items()
    kmers.sort(key = itemgetter(1), reverse =True)
    return kmers
        