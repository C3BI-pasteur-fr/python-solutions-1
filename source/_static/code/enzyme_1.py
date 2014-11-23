

def one_line(seq):
    return seq.replace('\n', '')

def enz_filter(enzymes, dna):
    cuting_enz = []
    for enz in enzymes:
        if enz.sequence in dna: 
            cuting_enz.append(enz)
    return cuting_enz

