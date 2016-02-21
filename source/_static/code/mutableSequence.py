


class NonMutableSequence(object):

    _water = 18.0153
    _alphabet = 'ACGT'

    def __init__(self, name, seq):
        """
        :param seq: the sequence
        :type seq: string
        """
        self.name = name
        self._sequence = seq

    @property
    def alphabet(self):
        return self._alphabet

    @property
    def sequence(self):
        return self._sequence


    def __len__(self):
        """
        :return: the length of this sequence (number of bases or aa)
        :rtype: integer
        """
        return len(self._sequence)


    def to_fasta(self):
        """
        :return: a string in fasta format of this sequence
        :rtype: basestring
        """
        id_ = self.name.replace(' ', '_')
        fasta = '>{}\n'.format(id_)
        start = 0
        while start < len(self._sequence):
            end = start + 80
            fasta += self._sequence[start: end + 1] + '\n'
            start = end
        return fasta


    def _one_strand_molec_weight(self, seq):
        """
        helper function to compute the mw of the seq
        :param seq: the seq (nucleic or proteic) to compute the mw
        :type seq: string
        :return: mw of seq
        :rtype: float
        """
        return sum([self._weight_table[base] for base in seq]) - (len(seq) - 1) * self._water


    def molecular_weight(self):
        """
        :return: The molecular weight
        :rtype: float
        """
        direct_weight = self._one_strand_molec_weight(self._sequence)
        rev_comp = self.rev_comp()
        rev_comp_weight = self._one_strand_molec_weight(rev_comp.sequence)
        return direct_weight + rev_comp_weight


    def rev_comp(self):
        """
        :return: a new sequence representing the reverse complement
        :rtype: :class:`Sequence` object
        """
        rev = self.sequence[::-1]
        table = str.maketrans(self._alphabet, self._alphabet[::-1])
        rev_comp = str.translate(rev, table)
        return self.__class__(self.name + '_reverse', rev_comp)


class Sequence(NonMutableSequence):


    def mutate(self, pos, base):
        """
        mutate the sequence replace the base at pos with base
        :param pos: the position of the base to mutate (starting count = 0)
        :type pos: integer
        :param base: the base to replace with it must be a char belonging to the alphabet
        :type base: string (one char)
        :return:
        """
        if base not in self._alphabet:
            raise ValueError("base must be {}".format(', '.join(["'{}'".format(c) for c in self._alphabet])))
        if pos < 0 or pos > len(self._sequence):
            raise ValueError("pos must be > 0 and < {}".format(len(self._sequence)))
        head = self._sequence[0:pos]
        tail = self._sequence[pos+1:]
        self._sequence = head + base + tail