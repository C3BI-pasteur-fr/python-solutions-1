from collections import namedtuple 

Sequence =  namedtuple("Sequence", "id comment sequence")

def fasta_reader(fasta_path):
    """
    :param fasta_path: the path to the file to parse
    :type fasta_path: string
    :return: the list of sequences read from the file
    :rtype: list of Sequence 
    """
    sequences = []
    with open(fasta_path, 'r') as fasta_infile:
        id_ = ''
        comment = ''
        sequence = ''
        for line in fasta_infile:
            if line.startswith('>'):
                # a new sequence begin
                if id_ != '':
                    # a sequence was already parsed so add it to the list
                    sequences.append(Sequence(id_ , comment, sequence))
                    sequence = ''
                header = line.split()
                id_ = header[0]
                comment = ' '.join(header[1:])
            else:
                sequence += line.strip()
                sequences.append(Sequence(id_ , comment, sequence))
    return sequences


# The problem with this implementation is that we have to load all 
# sequences in memory before to start to work with
# it is better to return sequence one by one
# and treat them as they are loaded.
 