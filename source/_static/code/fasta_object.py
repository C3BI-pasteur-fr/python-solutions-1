class Sequence(object):

    def __init__(self, id_, sequence, comment=''):
        self.id = id_
        self.comment = comment
        self.sequence = sequence


class FastaParser(object):


    def __init__(self, fasta_path):
        self.path = fasta_path
        self._file = open(fasta_path)
        self._current_id = ''
        self._current_comment = ''
        self._current_sequence = ''

    def _parse_header(self, line):
        """
        parse the header line and  _current_id|comment|sequence attributes
        :param line: the line of header in fasta format
        :type line: string
        """
        header = line.split()
        self._current_id = header[0][1:]
        self._current_comment = ' '.join(header[1:])
        self._current_sequence = ''

    def __iter__(self):
        return self

    def next(self):
        """
        :return: at each call return a new :class:`Sequence` object
        :raise: StopIteration
        """
        for line in self._file:
            if line.startswith('>'):
                # a new sequence begin
                if self._current_id != '':
                    new_seq = Sequence(self._current_id,
                                       self._current_sequence,
                                       comment=self._current_comment)
                    self._parse_header(line)
                    return new_seq
                else:
                    self._parse_header(line)
            else:
                self._current_sequence += line.strip()
        if not self._current_id and not self._current_sequence:
            self._file.close()
            raise StopIteration()
        else:
            new_seq = Sequence(self._current_id,
                               self._current_sequence,
                               comment=self._current_comment)
            self._current_id = ''
            self._current_sequence = ''
            return new_seq


if __name__ == '__main__':
    import sys
    import os.path

    if len(sys.argv) != 2:
        sys.exit("usage fasta_object fasta_path")
    fasta_path = sys.argv[1]
    if not os.path.exists(fasta_path):
        sys.exit("No such file: {}".format(fasta_path))

    fasta_parser = FastaParser(fasta_path)
    for sequence in fasta_parser:
        print "----------------"
        print sequence.id