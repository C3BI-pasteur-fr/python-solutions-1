class Sequence(object):

    def __init__(self, identifier, comment, seq):
        self.id = identifier
        self.comment = comment
        self.seq = self._clean(seq)


    def _clean(self, seq):
        """
        remove newline from the string representing the sequence
        :param seq: the string to clean
        :return: the string without '\n'
        :rtype: string
        """
        return seq.replace('\n')


    def gc_percent(self):
        """
        :return: the gc ratio
        :rtype: float
        """
        seq = self.seq.upper()
        return float(seq.count('G') + seq.count('C')) / len(seq)




dna1 = Sequence('gi214', 'the first sequence', 'tcgcgcaacgtcgcctacatctcaagattca')
dna2 = Sequence('gi3421', 'the second sequence', 'gagcatgagcggaattctgcatagcgcaagaatgcggc')