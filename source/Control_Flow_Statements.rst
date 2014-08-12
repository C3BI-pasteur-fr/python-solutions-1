.. _Control_Flow_Statements:


***********************
Control Flow Statements
***********************


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


::

   #This program calculates the Fibonacci sequence
   a = 0
   b = 1
   count = 0
   max_count = 10
   while count < max_count:
      count = count + 1
      print a,
      new_number = a + b
      #set new a and b for the next iteration
      a = b
      b = new_number 

We will see another way more elegant to implement the fibonacci suite in next chapter.


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

| which enzymes cut the dna_1 get the name of the enzymes and all their positions of binding site?
| do the same for dna_2
| give the name of the enzymes that cut the dna_1 but not the dna_2?

::

   dna_1 = dna_1.replace('\n', '')
   dans_2 = dna_2.replace('\n', '')

We looking for the first a cutting site, then we search again starting at the first nucleotid after the begining of the match 
until the end of the the dna, for this we use the start parameter of the find function, and so on. 
As we don't know how many loop we need to scan the dna until the end we use a ``while`` loop testing for the presence of a cutting site.::  
   
   enzymes = [ecor1, ecor5, bamh1, hind3, taq1, not1, sau3a1, hae3, sma1]
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
         
but we want also the position, for instance to compute the fragments of dna. ::

   digest_1 = []
   for enz in enzymes:
      pos = dna_1.find(enz.sequence)
      while pos != -1:
         digest_1.append((enz, pos))
         pos = dna_1.find(enz.sequence, pos + 1)
    
   #if we want to sort the list in function of their positions in the sequence 
   from operator import itemgetter
   digest_1.sort(key=itemgetter(1))
   print [(e.name, pos) for e, pos in digest_1]
   
   digest_2 = []
   for enz in enzymes:
      pos = dna_2.find(enz.sequence)
      while pos != -1:
         digest_2.append((enz, pos))
         pos = dna_2.find(enz.sequence, pos + 1)
   
   print "list of all enzymes cutting dna 1 and theirs position in dna1 :", [(e.name, pos) for e, pos in digest_1]
   print "list of all enzymes cutting dna 2 and theirs position in dna2 :", [(e.name, pos) for e, pos in digest_2]
           
   cut_dna_1 = set([e.name for e, pos in digest_1])
   cut_dna_2 = set([e.name for e, pos in digest_2])
   
   cut_dna_1_not_dna_2 = cut_dna_1 - cut_dna_2
   