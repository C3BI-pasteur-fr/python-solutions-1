from operator import itemgetter


def one_enz_binding_site(dna, enzyme):
    """
    return the first position of enzyme binding site in dna
    or None if there is not
    """
    pos = dna.find(enzyme.sequence)
    if pos != -1:
        return pos


def one_enz_binding_sites1(dna, enzyme):
    """
    return all positions of enzyme binding sites in dna
    """
    positions = []
    pos = dna.find(enzyme.sequence)
    if pos != -1:
        positions.append(pos)
        positions.extend(one_enz_binding_site1(dna[pos+1:], enzyme))
    return positions
        
        
def one_enz_binding_sites(dna, enzyme):
    """
    return all positions of enzyme binding sites in dna
    """
    positions = []
    pos = dna.find(enzyme.sequence)
    while pos != -1:
        positions.append(pos)
        pos = dna.find(enzyme.sequence, pos + 1)
    return positions


def binding_sites(dna, enzymes):
    """
    return all positions of all enzymes binding sites present in dna
    sort by the incresing position
    """
    positions = []
    for enzyme in enzymes:
        pos = one_enz_binding_sites(dna, enzyme)
        pos = [(enzyme.name, pos) for pos in pos]
        positions.extend(pos)
    positions.sort(key = itemgetter(1))
    return positions 

