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

* To compute the simalirity you need to parse a file containing the :download:`similarity matrix <_static/data/similarity_matrix>`.
  **Hint**: use the module containing the functions that handle a matrix from previous chapter.
  put this matrix.py file in a directory named "my_python_lib" in your home or Desktop
  and import it in your current program (the similarity script must be placed elsewhere).
* The similarity of the 2 sequences is the sum of base similarities. 
  so you have to compare the first base of two sequences and use the matrix to get the similarity
  from the similarity table, on so on for all bases then sum these similarities.

.. literalinclude:: _static/code/similarity.py
   :linenos:
   :language: python

:download:`similarity.py <_static/code/similarity.py>` .        