from collections import namedtuple 

Sequence =  namedtuple("Sequence", "id comment sequence")

def fasta_reader(fasta_path):
    """
    :param fasta_path: the path to the file to parse
    :type fasta_path: string
    :return: a sequence
    :rtype: Sequence instance
    """
    with open(fasta_path, 'r') as fasta_infile:
        id_ = ''
        comment = ''
        sequence = ''
        for line in fasta_infile:
            if line.startswith('>'):
                header = line.split()
                id_ = header[0]
                comment = ' '.join(header[1:])
            else:
                sequence += line.strip()
    return Sequence(id_ , comment, sequence)