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
   with open(fasta_path) as fasta_file:
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
         
#using exanple:
#f = fasta_iter('seq.fasta')
#f.next()
#or
# for seq in fasta_iter('seq.fasta'):
#   do something with seq
#The problem with this implementation is
# something goes wrong in do something with seq
# but we don't quit the program (we catch the exception for instance)
# the fasta file is still open
# it's better to put the fasta file opening out the fasta reader see fasta filter 