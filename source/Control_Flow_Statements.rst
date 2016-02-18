.. sectnum::
   :start: 7

.. _Control_Flow_Statements:


***********************
Control Flow Statements
***********************

Exercises
=========

Exercise
--------

The Fibonacci sequence are the numbers in the following integer sequence:

    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

By definition, the first two numbers in the Fibonacci sequence are 0 and 1, 
and each subsequent number is the sum of the previous two.
The fibonacci suite can be defined as following:

|    F\ :sub:`0` = 0, F\ :sub:`1` = 1. 
|    
|    F\ :sub:`n` = F\ :sub:`n-1` + F\ :sub:`n-2` 

Write a function which take an integer ``n`` as parameter
and returns a list containing the ``n`` first number of the Fibonacci sequence. 


.. literalinclude:: _static/code/fibonacci_iteration.py
   :linenos:
   :language: python
   
:download:`fibonacci_iteration.py <_static/code/fibonacci_iteration.py>` .
We will see another way more elegant to implement the fibonacci suite in :ref:`Advance Programming Techniques` section.



Exercise
--------

Reimplement your own function max (my_max).
This function will take a list or tuple of float or integer and 
returns the largest element?

Write the pseudocode before to propose an implementation.

pseudocode
^^^^^^^^^^

| *function my_max(l)*
|   *max <- first elt of l*
|   *for each elts of l*
|       *if elt is > max*
|       *max <- elt*
|   *return max*


implementation
^^^^^^^^^^^^^^

::

   def my_max(seq):
      """
      return the maximum value in a sequence 
      work only with integer or float
      """
      higest = seq[0]
      for i in seq:
         if i > highest:
             highest = i
      return highest
      
   l = [1,2,3,4,58,9]
   print my_max(l)
   58
   

.. _enzyme_exercise:

Exercise
--------

| We want to establish a restriction map of a sequence. 
| But we will do this step by step.
| and reuse the enzymes used in previous chapter: 

* create a function that take a sequence and an enzyme as parameter and return 
   the position of first binding sites.
   (write the pseudocode)

**pseudocode** 
   
| *function one_enz_binding_site(dna, enzyme)*
|     *if enzyme binding site is substring of dna*
|          *return of first position of substring in dna* 
 
**implementation**
 
.. literalinclude:: _static/code/restriction.py
   :linenos:
   :lines: 1-13
   :language: python
   
* improve the previous function to return all positions of binding sites

**pseudocode of first algorithm**

| *function one_enz_binding_sites(dna, enzyme)*
|     *positions <- empty*
|     *if enzyme binding site is substring of dna*
|          *add the position of the first substring in dna in positions* 
|     *positions <- find binding_sites in rest of dna sequence*
|     *return positions*  

**implementation**

.. literalinclude:: _static/code/restriction.py
   :linenos:
   :lines: 13-25
   :language: python

**pseudocode of second algorithm**

| *function one_enz_binding_sites(dna, enzyme)*
|     *positions <- empty*
|     *find first position of binding site in dna*
|     *while we find binding site in dna*
|         *add position of binding site to positions*
|         *find first position of binding site in dna in rest of dna*
|     *return positions*

**implementation**

.. literalinclude:: _static/code/restriction.py
   :linenos:
   :lines: 25-36
   :language: python
   
   
search all positions of Ecor1 binding sites in dna_1

::
 
   import collections
   RestrictEnzyme = collections.namedtuple("RestrictEnzyme", "name comment sequence cut end")

   ecor1 = RestrictEnzyme("EcoRI", "Ecoli restriction enzime I", "gaattc", 1, "sticky")
   
   dna_1 = """tcgcgcaacgtcgcctacatctcaagattcagcgccgagatccccgggggttgagcgatccccgtcagttggcgtgaattcag
   cagcagcgcaccccgggcgtagaattccagttgcagataatagctgatttagttaacttggatcacagaagcttccaga
   ccaccgtatggatcccaacgcactgttacggatccaattcgtacgtttggggtgatttgattcccgctgcctgccagg"""
   
   
* generalize the binding sites function to take a list of enzymes and return a list of tuple (enzyme name, position) 
   
**pseudocode**

| *function binding_sites(dna, set of enzymes)*
|     *positions <- empty*
|     *for each enzyme in enzymes*
|         *pos <- one_enz_binding_sites(dna, enzyme)*
|         *pos <- for each position create a tuple enzyme name, position*
|         *positions <- pos*
|     *return positions*

**implementation**

in bonus we can try to sort the list in the order of the position of the binding sites like this:
[('Sau3aI', 38), ('SmaI', 42), ('Sau3aI', 56), ('EcoRI', 75), ...

.. literalinclude:: _static/code/restriction.py
   :linenos:
   :lines: 37-
   :language: python
   
::
 
   import collections
   RestrictEnzyme = collections.namedtuple("RestrictEnzyme", "name comment sequence cut end")

   ecor1 = RestrictEnzyme("EcoRI", "Ecoli restriction enzime I", "gaattc", 1, "sticky")   
   ecor5 = RestrictEnzyme("EcoRV", "Ecoli restriction enzime V", "gatatc", 3, "blunt")
   bamh1 = RestrictEnzyme("BamHI", "type II restriction endonuclease from Bacillus amyloliquefaciens ", "ggatcc", 1, "sticky")
   hind3 = RestrictEnzyme("HindIII", "type II site-specific nuclease from Haemophilus influenzae", "aagctt", 1 , "sticky")
   taq1 = RestrictEnzyme("TaqI", "Thermus aquaticus", "tcga", 1 , "sticky")
   not1 = RestrictEnzyme("NotI", "Nocardia otitidis", "gcggccgc", 2 , "sticky")
   sau3a1 = RestrictEnzyme("Sau3aI", "Staphylococcus aureus", "gatc", 0 , "sticky")
   hae3 = RestrictEnzyme("HaeIII", "Haemophilus aegyptius", "ggcc", 2 , "blunt")
   sma1 =  RestrictEnzyme("SmaI", "Serratia marcescens", "cccggg", 3 , "blunt")

and the 2 dna fragments: ::

   dna_1 = """tcgcgcaacgtcgcctacatctcaagattcagcgccgagatccccgggggttgagcgatccccgtcagttggcgtgaattcag
   cagcagcgcaccccgggcgtagaattccagttgcagataatagctgatttagttaacttggatcacagaagcttccaga
   ccaccgtatggatcccaacgcactgttacggatccaattcgtacgtttggggtgatttgattcccgctgcctgccagg"""

   dna_2 = """gagcatgagcggaattctgcatagcgcaagaatgcggccgcttagagcgatgctgccctaaactctatgcagcgggcgtgagg
   attcagtggcttcagaattcctcccgggagaagctgaatagtgaaacgattgaggtgttgtggtgaaccgagtaag
   agcagcttaaatcggagagaattccatttactggccagggtaagagttttggtaaatatatagtgatatctggcttg"""

   enzymes= (ecor1, ecor5, bamh1, hind3, taq1, not1, sau3a1, hae3, sma1)
   binding_sites(dna_1, enzymes)
   [('Sau3aI', 38), ('SmaI', 42), ('Sau3aI', 56), ('EcoRI', 75), ('SmaI', 95), ('EcoRI', 105), 
   ('Sau3aI', 144), ('HindIII', 152), ('BamHI', 173), ('Sau3aI', 174), ('BamHI', 193), ('Sau3aI', 194)]

   binding_sites(dna_2, enzymes)
   [('EcoRI', 11), ('NotI', 33), ('HaeIII', 35), ('EcoRI', 98), ('SmaI', 106), 
   ('EcoRI', 179), ('HaeIII', 193), ('EcoRV', 225)]
   
:download:`restriction.py <_static/code/restriction.py>` .


Exercise
--------

From a list return a new list without any duplicate, but keeping the order of items. 
For example: ::

   >>> l = [5,2,3,2,2,3,5,1]
   >>> uniqify_with_order(l)
   >>> [5,2,3,1]  

solution ::

   >>> uniq = []
   >>> for item in l:
   >>>   if item not in uniq:
   >>>      uniq.append(item)

solution ::

   >>> uniq_items = set()
   >>> l_uniq = [x for x in l if x not in uniq_items and not uniq_items.add(x)]
     
 
