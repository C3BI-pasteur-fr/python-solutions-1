import collections

def kmer(sequence, k):
    kmers = collection.defaultdict(int)
    for i in range(len(sequence) - k):
        kmer = sequence[i:i + k]
        kmers[kmer] = kmers.get(kmer, 0) + 1
    return kmers