from collections import namedtuple 

Sequence =  namedtuple("Sequence", "id comment sequence")

def fasta_reader(fasta_path):
    with open(fasta_path, 'r') as fasta_infile:
        id = ''
        comment = ''
        sequence = ''
        in_sequence = False
        for line in fasta_infile:
            if line.startswith('>'):
                header = line.split()
                id = header[0]
                comment = ' '.join(header[1:])
                in_sequence = True
            elif in_sequence:
                sequence += line.strip()
            else:
                continue
        return Sequence(id , comment, sequence)