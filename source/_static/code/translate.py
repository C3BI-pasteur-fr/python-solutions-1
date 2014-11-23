genetic_code = {  'ttt': 'F', 'tct': 'S', 'tat': 'Y', 'tgt': 'C',
           'ttc': 'F', 'tcc': 'S', 'tac': 'Y', 'tgc': 'C',
           'tta': 'L', 'tca': 'S', 'taa': '*', 'tga': '*',
           'ttg': 'L', 'tcg': 'S', 'tag': '*', 'tgg': 'W',
           'ctt': 'L', 'cct': 'P', 'cat': 'H', 'cgt': 'R',
           'ctc': 'L', 'ccc': 'P', 'cac': 'H', 'cgc': 'R',
           'cta': 'L', 'cca': 'P', 'caa': 'Q', 'cga': 'R',
           'ctg': 'L', 'ccg': 'P', 'cag': 'Q', 'cgg': 'R',
           'att': 'I', 'act': 'T', 'aat': 'N', 'agt': 'S',
           'atc': 'I', 'acc': 'T', 'aac': 'N', 'agc': 'S',
           'ata': 'I', 'aca': 'T', 'aaa': 'K', 'aga': 'R',
           'atg': 'M', 'acg': 'T', 'aag': 'K', 'agg': 'R',
           'gtt': 'V', 'gct': 'A', 'gat': 'D', 'ggt': 'G',
           'gtc': 'V', 'gcc': 'A', 'gac': 'D', 'ggc': 'G',
           'gta': 'V', 'gca': 'A', 'gaa': 'E', 'gga': 'G',
           'gtg': 'V', 'gcg': 'A', 'gag': 'E', 'ggg': 'G'
      }

def translate(nuc_seq, code):
    
    prot_seq = ''
    n = 0
    # to avoid to compute len(seq)/3 at each loop
    # I compute it once and use a reference
    # it could be expensive if the sequence is very long.
    cycle = len(nuc_seq)/3
    while n < cycle:
        start = n * 3
        end = start + 3
        codon = nuc_seq[start:end]
        codon = codon.lower()
        if codon in code:
            prot_seq += code[codon] 
        else:
            raise RuntimeError("unknow codon: " + codon)
        n += 1
    return prot_seq
        
def translate2(nuc_seq, code, phase = 1):
    prot_seq = ''
    if 0 < phase < 4 :
        start = phase - 1
    elif -4 < phase < 0:
        start = -phase - 1
        nuc_seq = nuc_seq[::-1]
    # an other way to determine the end of looping
    stop_iteration = len(nuc_seq)
    while (start + 2) < stop_iteration:
        end = start + 3
        codon = nuc_seq[start:end].lower()
        if codon in code:
            prot_seq += code[codon] 
        else:
            raise RuntimeError("unknow codon")
        start += 3        
    return prot_seq
