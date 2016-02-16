



class Matrix(object):

    def __init__(self, row, col, val=None):
        self._row = row
        self._col = col
        self._matrix = []
        for i in range(row):
            c = [val] * col
            self._matrix.append(c)

    def size(self):
        return self._row, self._col

    def get_cell(self, row, col):
        self._check_index(row, col)
        return self._matrix[i][j]

    def matrix_set(self, row, col, val):
        self._check_index(row, col)
        self._matrix[row][col] = val

    def __str__(self):
        s = ''
        for i in range(self._row):
            s += self._matrix[i]
            s += '\n'
        return s

    def _check_index(self, row, col):
        if not (0 < row <= self._row) or not (0 < col <= self._col):
            raise IndexError("matrix index out of range")
