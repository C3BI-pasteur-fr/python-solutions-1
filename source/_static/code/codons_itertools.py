from itertools import product

def all_codons():
    alphabet = 'acgt'
    all_codons = [ ''.join(codon) for codon in product(alphabet, repeat = 3)]
    return all_codons