from collections import namedtuple 

Sequence =  namedtuple("Sequence", "id comment sequence")

def fasta_reader(fasta_file):
    """
    :param fasta_path: the path to the file to parse
    :type fasta_path: string
    :return: the list of sequences read from the file
    :rtype: list of Sequence 
    """
    sequences = []
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
    return Sequence(id_ , comment, sequence)

# if we open the file in the fasta reader we are forced
# to read all the sequences and charge them in memory which can take huge space
# it's better to read sequences one by one and treat it as one is ready.
# see fasta_filter.py