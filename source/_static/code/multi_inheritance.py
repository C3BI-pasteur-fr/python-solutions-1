from abc import ABCMeta, abstractmethod


class BaseSequence(object, metaclass=ABCMeta):

    _water = 18.0153

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


    @abstractmethod
    def molecular_weight(self):
        """
        tihis method is abstract and must be implemented in child classes
        :return: The molecular weight
        :rtype: float
        """
        pass


class Mutable(object):


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


class NonMutableDNASequence(BaseSequence):

    _weight_table = {'A': 347.2212, 'C': 323.1965, 'G': 363.2206, 'T': 322.2085}
    _alphabet = 'ACGT'

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


class MutableDNASequence(NonMutableDNASequence, Mutable):

    pass


class NonMutableAASequence(BaseSequence):

    _weight_table = {'A': 89.0932, 'C': 121.1582, 'E': 147.1293,
                     'D': 133.1027, 'G': 75.0666, 'F': 165.1891,
                     'I': 131.1729, 'H': 155.1546, 'K': 146.1876,
                     'M': 149.2113, 'L': 131.1729, 'O': 255.3134,
                     'N': 132.1179, 'Q': 146.1445, 'P': 115.1305,
                     'S': 105.0926, 'R': 174.201, 'U': 168.0532,
                     'T': 119.1192, 'W': 204.2252, 'V': 117.1463,
                     'Y': 181.1885}

    _alphabet = ''.join(_weight_table.keys())

    def molecular_weight(self):
        """
        :return: The molecular weight
        :rtype: float
        """
        return super()._one_strand_molec_weight(self.sequence)


class MutableAASequence(NonMutableAASequence, Mutable):

    pass