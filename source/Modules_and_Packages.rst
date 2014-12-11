.. sectnum::
   :start: 9

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
The API (**A**\ pplication **P**\ rogramming **I**\ nterface) to implement is the following:

We propose 2 implementations. These 2 implementations work with a list of lists as matrix modelling.
But it is possible to implement it with a single list or a dict of list, ...

The first implementation follow the api used explicit name for inner variables and good documentation. 
         
.. literalinclude:: _static/code/matrix.py
   :linenos:
   :language: python

:download:`matrix.py <_static/code/matrix.py>` .  

But the problem with this implementation is, if we decide to change the inner model for a dixt of list for instance.
We must reimplements most of the functions.

In the following implementation we have only 4 functions that handle directly the lists. All other functions
manipulate the matrix through these 4 functions. So if we change the inner model we will have to modifiy 
only these functions. This implementation will be more maintainable.


But this implementation use one letter names for inner variables and is poorly documented which not help
to maintain or develop with this.

The Best solution should be the second implementation but with the name of variables and documentation as in the firsr 
implementation.

.. literalinclude:: _static/code/matrix2.py
   :linenos:
   :language: python

:download:`matrix2.py <_static/code/matrix2.py>` .


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