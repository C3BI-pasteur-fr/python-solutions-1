
class Sequence(object):

    def __init__(self, identifier, comment, seq):
        self.id = identifier
        self.comment = comment
        self.seq = self._clean(seq)


    def _clean(self, seq):
        """

        :param seq:
        :return:
        """
        return seq.replace('\n')

    def enzyme_filter(self, enzymes):
        """

        :param enzymes:
        :return:
        """
        enzymes_which_binds = []
        for enz in enzymes:
            if enz.binds(self.seq):
                enzymes_which_binds.append(enz)
        return


class RestrictionEnzyme(object):

    def __init__(self, name, binding, cut, end, comment=''):
        self.name = name
        self.binding = binding
        self.cut = cut
        self.end = end
        self.comment = comment


    def binds(self, seq):
        """

        :param seq:
        :return:
        """
        return self.binding in seq.seq