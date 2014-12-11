"""
Implementation of simple matrix 
"""


def create(row_num, col_num, val = None):
	"""
	:param row_num: the number of rows
	:type row_num: int
	:param col_num: the number of columns
	:type col_num: int
	:param val: the default value to fill the matrix
	:type val: any (None by default)
	:return: matrix of rows_num x col_num
	:rtype: matrix
	"""
	matrix = []
	for i in range(col_num):
		col = [val] * row_num
		matrix.append(col)
	return matrix


def _check_index(matrix, row_no, col_no):
	"""
	check if row_no and col_no are in matrix bound
	
	:param matrix: the matrix to compute the size
	:type matrix: matrix
	:param rows_no: the index of row to check
	:type rows_no: int
	:param col_no: the index of column to check
	:type col_no: int
	:raise: IndexError if row_no or col_no are out of matrix bounds
	""" 
	row_max, col_max = size(matrix)
	if (row_no < 0 or row_no >= row_max) or (col_no < 0 or col_no >= col_max):
		raise IndexError("matrix index out of range")
	
	
def size(matrix):
	"""
	:param matrix: the matrix to compute the size
	:type matrix: matrix
	:return: the size of matrix (number of rows, number of cols)
	:rtype: typle of 2 int
	"""
	return len(matrix[0]), len(matrix)


def get_cell(matrix, row_no, col_no):
	"""
	:param matrix: the matrix 
	:type matrix: matrix
	:param rows_no: the row number
	:type rows_no: int
	:param col_no: the column number
	:type col_no: int
	:retrun: the content of cell corresponding to row_no x col_no
	:rtype: any
	"""
	_check_index(matrix, row_no, col_no)
	return matrix[col_no][row_no]


def set_cell(matrix, row_no, col_no, val):
	"""
	set the value val in cell specified by row_no x col_no
	
	:param matrix: the matrix to modify
	:type matrix: matrix
	:param row_no: the row number of cell to set
	:type rows_no: int
	:param col_no: the column number of cell to set
	:type col_no: int
	:param val: the value to set in cell 
	:type val: int
	"""
	_check_index(matrix, row_no, col_no)
	matrix[col_no][row_no] = val


def to_str(matrix):
	"""
	:param matrix: the matrix to compute the size
	:type matrix: matrix
	:return: a string representation of the matrix
	:rtype: str
	"""
	s = ""
	# by design all matrix cols have same size
	for row in zip(*matrix):
		cells = [str(cell) for cell in row]
		s += " ".join(cells) + "\n"
	return s


def mult(matrix, val):
	"""
	:param matrix: the matrix to compute the size
	:type matrix: matrix
	:param rows_no: the number of rows
	:type rows_no: int
	:param col_no: the number of columns
	:type col_no: int
	:param val: the value to mult the matrix with
	:type val: int
	:return: a new matrix corresponding the scalar product of matrix * val
	:rtype: matrix
	"""
	new_matrix = []
	for col in matrix:
		new_col = [cell * val for cell in col]
		new_matrix.append(new_col)
	return new_matrix


def get_row(matrix, row_no):
	"""
	:param matrix: the matrix to compute the size
	:type matrix: matrix
	:param rows_no: row number
	:type rows_no: int
	:return: the row of matrix corresponding to row_no
	         a shallow copy of the row
	:rtype: list
	"""
	_check_index(matrix, row_no, 0)
	row_max, col_max = size(matrix)
	row = []
	for col_n in range(col_max):
		row.append(get_cell(matrix, row_no, col_n))
	return row
	
	
def set_row(matrix, row_no, val):
	"""
	set all cells of row row_no with val
	
	:param matrix: the matrix to modify
	:type matrix: matrix
	:param row_no: the row number
	:type row_no: int
	:param val: the value to put in cells
	:type val: any
	"""
	_check_index(matrix, row_no, 0)
	row_max, col_max = size(matrix)
	for col_n in range(col_max):
		set_cell(matrix, row_no, col_n, val)


def get_col(matrix, col_no):
	"""
	:param matrix: the matrix get row
	:type matrix: matrix
	:param col_no: the column number
	:type col_no: int
	:return: the column corresponding to col_no of matrix
	         a shallow copy of the col
	:rtype: list
	"""
	_check_index(matrix, 0, col_no)
	col = matrix[col_no][:]
	return col
	
	
def set_col(matrix, col_no, val):
	"""
	set all cells of col col_no with val
	
	:param matrix: the matrix to compute the size
	:type matrix: matrix
	:param col_no: the column number
	:type col_no: int
	:param val: the value to put in cells
	:type val: any
	"""
	_check_index(matrix, 0, col_no)
	row_max, col_max = size(matrix)
	for row_n in range(im):
		set_cell(matrix, row_n, col_no, val)


def replace_col(matrix, col_no, col):
	"""
	replace column col_no with col
	
	:param matrix: the matrix to compute the size
	:type matrix: matrix
	:param col_no: the column number to replace
	:type col_no: int
	:param col: the list of values to use as replacement of column 
	:type col: list
	"""
	row_max, col_max = size(matrix)
	if len(col) != col_max:
		raise RuntimeError("the size of col {0} does not fit to matrix size {1}x{2}".format(len(col),
																						row_max,
																						col_max))
	_check_index(matrix, 0, col_no)
	matrix[col_no] = col


def replace_row(matrix, row_no, row):
	"""
	replace row row_no with row
	
	:param matrix: the matrix to compute the size
	:type matrix: matrix
	:param row_no: the column number
	:type row_no: int
	:param row: the list of value to use as replacement of row 
	:type row: list
	"""
	row_max, col_max = size(matrix)
	if len(row) != row_max:
		raise RuntimeError("the size of row {0} does not fit to matrix size {1}x{2}".format(len(row),
																						row_max,
																						col_max))
	_check_index(matrix, row_no, 0)
	for col_no, value in enumerate(row):
		set_cell(matrix, row_no, col_no, value)

		
	
if __name__ == '__main__':
	m = create(5, 3)
	print m
	set_cell(m,0, 0, 1)
	set_cell(m,0, 2, 2)
	set_cell(m,4, 0, 12)
	set_cell(m,4, 2, 15)
	print to_str(m)
	print "get row 0",  get_row(m, 0)
	print "get col 0", get_col(m, 0)
	
