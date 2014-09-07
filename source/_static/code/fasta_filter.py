import sys
import os
from collections import namedtuple 
from itertools import groupby
   
Sequence =  namedtuple("Sequence", "id comment sequence")

def fasta_iter(fasta_file):
    """
    :param fasta_file: the file containing all input sequences in fasta format.
    :type fasta_file: file object
    :author: http://biostar.stackexchange.com/users/36/brentp
    :return: for a given fasta file, it returns an iterator which yields tuples
          (string id, string comment, int sequence length)
    :rtype: iterator
    """
    # ditch the boolean (x[0]) and just keep the header or sequence since
    # we know they alternate.
    group = (x[1] for x in groupby(fasta_file , lambda line: line[0] == ">"))
    for header in group:
       # drop the ">"
       header = header.next()[1:].strip()
       header = header.split()
       _id = header[0]
       comment = ' '.join(header[1:])
       seq = ''.join(s.strip() for s in group.next())
       yield Sequence(_id, comment, seq)
         
         
def fasta_writer(sequence, output_file):
    """
    write a sequence in a file in fasta format

    :param sequence: the sequence to print
    :type sequence: Sequence instance
    :param v: the file to print the sequence in
    :type output_file: file object
    """
    output_file.write('>{0.id} {0.comment}\n'.format(seq))
    start = 0
    while start < len(seq.sequence):
        end = start + 80
        print start, " : ", end
        output_file.write(seq.sequence[start: end + 1] + '\n')
        start = end


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit("usage: fasta_filter path/to/fasta/file/to/read")
    input_path = sys.argv[1]
    
    with open(input_path, 'r') as input_file:
        for seq in fasta_iter(input_path):
            if seq.sequence.startswith('M') and seq.sequence.count('W') > 6:
                if os.path.exists(seq.id):
                    print >> sys.stderr , "file {0} already exist: sequence {0} skipped".format(seq.id)
                    continue
                else:
                    output_fasta = seq.id + ".fa"
                    with open(output_path, 'w') as output_file:
                        fasta_writer(seq, output_file)