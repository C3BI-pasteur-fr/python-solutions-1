.. sectnum::
   :start: 14


.. _Architecture_and_Design:

***********************
Architecture and Design
***********************


Exercises
=========

Exercise
--------

Create 2 classes

 * Sequence
 * MutableSequence

These 2 classes have same attributes but MutableSequence can be mutate and extend whereas Sequence are immutable.

example of code using these classes: ::

    >>> eco = MutableSequence('toto' , 'GAATTC')
    >>> eco.mutate(1, 'T')
    >>> eco.sequence
    'GTATTC'
    >>> eco.mutate(10, 'T')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "mutableSequence.py", line 97, in mutate
        raise ValueError("pos must be >0 and < {}".format(len(self._sequence)))
    ValueError: pos must be >0 and < 6


Exercise
--------

how can you modeling

    * non mutable DNA sequence
    * mutable DNA sequence
    * non mutable amino acid sequence
    * mutable amino acid sequence

**bonus**: can you easily extend your model to support no mutable/ mutable RNA sequence ?


.. literalinclude:: _static/code/multi_inheritance.py
   :linenos:
   :language: python

:download:`multi_inheritance.py <_static/code/multi_inheritance.py>`

Exercise
--------

work with in small groups (2-3 people).
To solve a problem we need to design

    * genome
    * gene
    * sequence

in context in eukaryote and prokaryote. propose an architecture. you hav not to implement methods just
do a schema of the components and the relations between the components.

    .. note::
        you can add objects not listed above if you need for your architecture.

