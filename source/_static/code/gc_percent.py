
def gc_percent(seq):
    gc_pc =  float(seq.count('g') + seq.count('c')) / float(len(seq))
    return gc_pc