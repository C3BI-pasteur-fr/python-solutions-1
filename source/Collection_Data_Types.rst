.. sectnum:: 
   :start: 4


.. _Collection_Data_types:

*********************
Collection Data Types
*********************

Exercices
=========

exercice
--------

From a list return a new list without any duplicate, regardless of the order of items. 
For example: ::

   >>> l = [5,2,3,2,2,3,5,1]
   >>> uniqify(l)
   >>> [1,2,3,5] #is one of the solutions 

solution ::

   >>> list(set(l))


exercice
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
   
exercice
--------

list and count occurences of every 3mers in the following sequence ::

   s = """gtcagaccttcctcctcagaagctcacagaaaaacacgctttctgaaagattccacactcaatgccaaaatataccacag
   gaaaattttgcaaggctcacggatttccagtgcaccactggctaaccaagtaggagcacctcttctactgccatgaaagg
   aaaccttcaaaccctaccactgagccattaactaccatcctgtttaagatctgaaaaacatgaagactgtattgctcctg
   atttgtcttctaggatctgctttcaccactccaaccgatccattgaactaccaatttggggcccatggacagaaaactgc
   agagaagcataaatatactcattctgaaatgccagaggaagagaacacagggtttgtaaacaaaggtgatgtgctgtctg
   gccacaggaccataaaagcagaggtaccggtactggatacacagaaggatgagccctgggcttccagaagacaaggacaa
   ggtgatggtgagcatcaaacaaaaaacagcctgaggagcattaacttccttactctgcacagtaatccagggttggcttc
   tgataaccaggaaagcaactctggcagcagcagggaacagcacagctctgagcaccaccagcccaggaggcacaggaaac
   acggcaacatggctggccagtgggctctgagaggagaaagtccagtggatgctcttggtctggttcgtgagcgcaacaca"""

and finally print the results one 3mer and it's occurence per line. 

write first the pseudocode, then implement it.

bonus:
print the kmer by incresing occurences.

solution ::

   s = s.replace('\n', '')
   kmers = {}
   for i in range(len(s) - 3):
      kmer = s[i:i+3]
      kmers[kmer] = kmers.get(kmer, 0) + 1

   for kmer, occurence in kmers.items():
      print kmer, " = ", occurence

solution bonus ::

   list_of_kmers = kmers.items()  
   from operator import itemgetter
   list_of_kmers.sort(key=itemgetter(1)) 
   for kmer, occurence in list_of_kmers:
      print kmer, " = ", occurence

 solution bonus ::

   list_of_kmers = kmers.items()      
   list_of_kmers.sort(key = lambda kmer: kmer[1])
   for kmer, occurence in list_of_kmers:
      print kmer, " = ", occurence   
      
      
exercice
--------

given the following dict : ::

   d = {1 : 'a', 2 : 'b', 3 : 'c' , 4 : 'd'}
   
We want obtain a new dict with the keys and the values inverted so we will obtain: ::

   inverted_d  {'a': 1, 'c': 3, 'b': 2, 'd': 4}

solution ::

   inverted_d = {}
   for key in d.keys():
       inverted_d[d[key]] = key
       
solution ::

   inverted_d = {v : k for k, v in d.items()}