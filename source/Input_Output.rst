.. sectnum::
   :start: 10

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
and return in a dictionary the collection of the enzyme contains in the file.
The sequence of the binding site must be cleaned up.

use the file :download:`rebase_light.txt <_static/data/rebase_light.txt>` to test your code.

.. literalinclude:: _static/code/rebase.py
   :linenos:
   :language: python

:download:`rebase.py <_static/code/rebase.py>` .
 
Exercise
--------

write a function which take the path of a fasta file (containing only one sequence) 
and return a data structure of your choice that allow to stock 
the id of the sequence and the sequence itself.

use the file :download:`seq.fasta <_static/data/seq.fasta>` to test your code.

.. literalinclude:: _static/code/fasta_reader.py
   :linenos:
   :language: python

:download:`fasta_reader.py <_static/code/fasta_reader.py>` .   

Exercise
--------

Modify the code at the previous exercise to read multiple sequences fasta file.
use the file :download:`abcd.fasta <_static/data/abcd.fasta>` to test your code.

solution 1
^^^^^^^^^^
.. literalinclude:: _static/code/multiple_fasta_reader.py
   :linenos:
   :language: python

:download:`multiple_fasta_reader.py <_static/code/multiple_fasta_reader.py>` 

solution 2
^^^^^^^^^^
.. literalinclude:: _static/code/multiple_fasta_reader2.py
   :linenos:
   :language: python

:download:`multiple_fasta_reader2.py <_static/code/multiple_fasta_reader2.py>` 

solution 3
^^^^^^^^^^
.. literalinclude:: _static/code/fasta_iterator.py
   :linenos:
   :language: python

:download:`fasta_iterator.py <_static/code/fasta_iterator.py>` .   
   
With the first version, we have to load all sequences before to treat them.
if the file is huge (>G0) it can be a problem.

The third version allow to red sequences one by one.
To do that we have to open the file outside the reader function
The fasta format is very convenient for human but not for parser.
The end of a sequence is indicated by the end of file or the begining of a new one.
So with this version we have play with the cursor to place the cursor backward
when we encouter a new sequence. then the cursor is placed at the right place 
for the next sequence.

    
The third version  is an iterator and use generator. 
generators are functions which keep a state between to calls.
generators does not use return to return a value but the keyword yield.
Thus this implementation retrun sequence by sequence without to play with the cursor.
You can call this function and put in in a loop or call next. 
Work with the sequence and pass to the next sequence on so on.
for instance which is a very convenient way to use it: ::
   
   for seq in fasta_iter('my_fast_file.fasta'):
      print seq
    

Exercise
--------

Read a multiple sequence file in fasta format and write to a new file, one sequence by file,
only sequences starting with methionine and containing at least six tryptophanes (W).
 
(*you should create files for sequences: ABCD1_HUMAN, ABCD1_MOUSE, ABCD2_HUMAN, ABCD2_MOUSE, ABCD2_RAT, ABCD4_HUMAN, ABCD4_MOUSE*)

bonus
^^^^^

Write sequences with 80 aa/line

.. literalinclude:: _static/code/fasta_filter.py
   :linenos:
   :language: python

:download:`fasta_iterator.py <_static/code/fasta_filter.py>` .

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

(adapted from *managing your biological data with python* p138) 

.. literalinclude:: _static/code/parse_blast.py
   :linenos:
   :language: python

:download:`parse_blast.py <_static/code/parse_blast.py>` .   