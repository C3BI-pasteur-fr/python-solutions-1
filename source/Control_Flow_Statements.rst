.. sectnum:: 
   :start: 6
   

.. _Control_Flow_Statements:


***********************
Control Flow Statements
***********************

Exercises
=========

Exercise
--------

Calculates the 10 first number of the Fibonacci sequence .
The Fibonacci sequence are the numbers in the following integer sequence:

    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

By definition, the first two numbers in the Fibonacci sequence are 0 and 1, 
and each subsequent number is the sum of the previous two.
The fibonacci suite can be defined as following:

|    F\ :sub:`0` = 0, F\ :sub:`1` = 1. 
|    
|    F\ :sub:`n` = F\ :sub:`n-1` + F\ :sub:`n-2` 

.. literalinclude:: _static/code/fibonacci_iteration.py
   :linenos:
   :language: python
   
 
Exercise
--------

let the following enzymes collection: ::
 
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

| which enzymes cut the dna_1 ?
|                  the dna_2 ?
|                  the dna_1 but not the dna_2?

::

   dna_1 = dna_1.replace('\n', '')
   dans_2 = dna_2.replace('\n', '')
   
   enzymes = [ecor1, ecor5, bamh1, hind3, taq1, not1, sau3a1, hae3, sma1]
   digest_1 = []
   for enz in enzymes:
      pos = dna_1.find(enz.sequence)
      if pos != -1:
         digest_1.append(enz)

with this first algorithm we find if an enzyme cut the dna but we cannot find all cuts in the dna for an enzyme.
If we find a cutting site, we must search again starting at the first nucleotid after the begining of the match 
until the end of the the dna, for this we use the start parameter of the find function, and so on. 
As we don't know how many loop we need to scan the dna until the end we use a ``while`` loop testing for the presence of a cutting site.::  

   digest_1 = []
   for enz in enzymes:
      pos = dna_1.find(enz.sequence)
      while pos != -1:
         digest_1.append(enz)
         pos = dna_1.find(enz.sequence, pos + 1)
         
   digest_2 = []
   for enz in enzymes:
      pos = dna_2.find(enz.sequence)
      while pos != -1:
         digest_2.append(enz)
         pos = dna_2.find(enz.sequence, pos + 1)  
                
   cut_dna_1 = set(digest_1)
   cut_dna_2 = set(digest_2)
   cut_dna_1_not_dna_2 = cut_dna_1 - cut_dna_2
         
If we want also the position, for instance to compute the fragments of dna. ::

   digest_1 = []
   for enz in enzymes:
      pos = dna_1.find(enz.sequence)
      while pos != -1:
         digest_1.append((enz, pos))
         pos = dna_1.find(enz.sequence, pos + 1)
    
   from operator import itemgetter
   digest_1.sort(key=itemgetter(1))
   [(e.name, d) for e, d in digest_1]
   
   digest_2 = []
   for enz in enzymes:
      pos = dna_2.find(enz.sequence)
      while pos != -1:
         digest_2.append((enz, pos))
         pos = dna_2.find(enz.sequence, pos + 1)
           
   cut_dna_1 = set([e.name for e in digest_1])
   cut_dna_2 = set([e.name for e in digest_2])
   cut_dna_1_not_dna_2 = cut_dna_1 - cut_dna_2
   

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
     
 