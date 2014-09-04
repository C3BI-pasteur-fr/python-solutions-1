.. _Creating_and_Calling_Functions:

******************************
Creating and Calling Functions
******************************

Exercises
=========


Exercice
--------

Use the code of the exetrcise 4.5.7 on the kmer. Make a function which compute all kmer of a given lenght
in a sequence.

.. literalinclude:: _static/code/kmer.py
   :linenos:
   :language: python

:download:`kmer.py <_static/code/kmer.py>` .

Exercise
--------

Write a function translate that have a nucleic sequence as parameter, and return the translate sequence.
We give you a genetic code : ::
  
   code = {  'ttt': 'F', 'tct': 'S', 'tat': 'Y', 'tgt': 'C',
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

bonus
"""""

This function have to take the phase as parameter

.. literalinclude:: _static/code/translate.py
   :linenos:
   :language: python

:download:`translate.py <_static/code/translate.py>` .  

Exercise
--------

Implement a matrix and functions to handle it.
choose the data structure of your choice.
The API (**A**\ pplication **P**\ rogramming **I**\ nterface) to implemet is the following:

         
.. literalinclude:: _static/code/matrix.py
   :linenos:
   :language: python

:download:`matrix.py <_static/code/matrix.py>` .  

Exercise
--------

Write a program that calculates the similarity of 2 RNA sequences.

* To compute the simalirity you need to parse a file containing the similarity matrix.
* The similarity of the 2 sequences is the sum of base similarities. 
  so you have to compare the first base of to sequence and use the matrix to get the similarity
  from the similarity table, on so on for all bases then sum these similarities.
  
.. note::
   as we  don't yet see how to read a file, we provide a list of strings that represents the file
   as we can get them if we read that file.
   
::

   lines = iter(['  A G C U\n'
                 'A 1.0 0.5 0.0 0.0\n',
                 'G 0.5 1.0 0.0 0.0\n',
                 'C 0.0 0.0 1.0 0.5\n',
                 'U 0.0 0.0 0.5 1.0\n'])

.. literalinclude:: _static/code/similarity.py
   :linenos:
   :language: python

:download:`similarity.py <_static/code/similarity.py>` .            