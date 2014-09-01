.. _Input_Output:

****************
Input and Output
****************

Exercises
=========

Exercise
--------

Write a function which take the path of file as parameter
and display it's content on the screen.

We wait same behavior as the shell *cat* command. ::

   import sys
   import os
   
   def cat(path):
      if not os.path.exists(path):
         sys.exit("no such file: {0}".format(path)
      with open(path, 'r') as infile:
         for line in infile:
            print line
         
Exercise
--------

Write a function which take the path of a file in rebase format
and return in a dictionnary the collection of the enzyme contains in the file.
The sequence of the binding site must be cleaned up.

:download:`rebase_light.txt <_static/data/rebase_light.txt>` .
 
Exercise
--------

write a function which take the path of a fasta file
and return a data structure of your choice that allow to stock 
the id of the sequence and the sequence itself.

:download:`seq.fasta <_static/data/seq.fasta>` .

solution 1
""""""""""
.. literalinclude:: _static/code/fasta_reader.py
   :linenos:
   :language: python

:download:`fasta_reader.py <_static/code/fasta_reader.py>` .   

solution 2
""""""""""

.. literalinclude:: _static/code/fasta_iterator.py
   :linenos:
   :language: python

:download:`fasta_iterator.py <_static/code/fasta_iterator.py>` .   
   
   
The second version  is an iterator. Thus it retrun sequence by sequence the advantage of this version. 
If the file contains lot of sequences you have not to load all the file in memory.
You can call this function and put in in a loop or call next. work with the sequence and pass to the next sequence on so on.
for instance : ::
   
   for seq in fasta_iter('my_fast_file.fasta'):
      print seq
    
Exercise
--------

we ran a blast with the folowing command *blastall -p blastp -d uniprot_sprot -i query_seq.fasta -e 1e-05 -m 8 -o blast2.txt*

-m 8 is the tabular output. So each fields is separate to the following by a '\t' 

The fields are: query id, database sequence (subject) id, percent identity, alignment length, number of mismatches, number of gap openings, 
query start, query end, subject start, subject end, Expect value, HSP bit score. 

:download:`blast2.txt <_static/data/blast2.txt>` .

| parse the file
| sort the hits by their *percent identity* in the descending order.
| write the results in a new file.

(adapted from *managing your biological data with python* p138) ::

.. literalinclude:: _static/code/parse_blast_output.py
   :linenos:
   :language: python

:download:`parse_blast_output.py <_static/code/parse_blast_output.py>` .   