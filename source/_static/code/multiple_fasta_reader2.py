from collections import namedtuple 

Sequence =  namedtuple("Sequence", "id comment sequence")

def fasta_reader(fasta_file):
    """
    :param fasta_file: to the file in fasta format to parse
    :type fasta_file: file object
    :return: a sequence until they are sequences in the file
    :rtype: a Sequence or None
    """
    id_ = ''
    comment = ''
    sequence = ''
    # As we use seek or tell, we cannot use for line in file object
    # Because in the last case tell is always at the end of file
    # even if when we read the first line
    # So I use readline
    line = fasta_file.readline()
    while line:
        if line.startswith('>'):
            # a new sequence begin
            if id_ == '':
                header = line.split()
                id_ = header[0]
                comment = ' '.join(header[1:])
            else:
                # I already parse a sequence
                # So the beginning of this sequence indicate the end of the
                # previous sequence
                # put the cursor one line in back for the next fasta_reader call
                fasta_file.seek(-len(line),1)
                # I return the previous sequence
                return Sequence(id_ , comment, sequence)
        else:
            sequence += line.strip()
        line = fasta_file.readline()
    if id_ == '' and sequence == '':
        return 
    else:
        return Sequence(id_ , comment, sequence)


# to return sequence by sequence we had to open the file outside the fasta_reader
# at each fasta_reader call the function return one sequence
# unitl the end of file

if __name__ == '__main__':
    import sys
    import os.path
    
    if len(sys.argv) != 2:
        sys.exit("usage multiple_fasta fasta_path")
    fasta_path = sys.argv[1]
    if not os.path.exists(fasta_path):
        sys.exit("No such file: {}".format(fasta_path))
        
    with open(fasta_path, 'r') as fasta_input:    
        sequence = True
        while sequence is not None:
            sequence =  fasta_reader(fasta_input)
            print "----------------"
            print sequence
            