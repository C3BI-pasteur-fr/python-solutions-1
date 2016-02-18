
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
        self._name = name
        self._binding = binding
        self._cut = cut
        self._end = end
        self._comment = comment

    @property
    def name(self):
        return self._name

    def binds(self, seq):
        """

        :param seq:
        :return:
        """
        return self.binding in seq.seq