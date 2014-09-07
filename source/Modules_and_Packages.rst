.. _Modules_and_Packages:

********************
Modules and Packages
********************

Exercises
=========


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