
def all_codons():
    all_codons = []
    alphabet = 'acgt'
    for base_1 in alphabet:
        for base_2 in alphabet:
            for base_3 in alphabet:
                codon = base_1 + base_2 + base_3
                all_codons.append(codon)
    return all_codons