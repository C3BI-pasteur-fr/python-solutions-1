# matrix is implemented by list of list
def matrix_maker(ligne, col, val=None):
	m = []
	for i in range(ligne):
		c = [val]*col
		m.append(c)
	return m

#---- functions that depends on the matrix srtructure 

def matrix_size(m):
	return len(m), len(m[0])

def matrix_get(matrix, i, j):
	_check_matindex(matrix,i,j)
	return matrix[i][j]

def matrix_set(matrix, i, j, val):
	_check_matindex(matrix,i,j)
	matrix[i][j] = val

def matrix_print(m):
	im, jm = matrix_size(m) 
	for i in range(im):
		print m[i]



#---- independant regarding matrix structure  
def _check_matindex(matrix,i,j):
	imax, jmax = matrix_size(matrix)
	if (i < 0 or i >= imax) or (j < 0 or j>= jmax):
		raise IndexError, "matrix index out of range"



def matrix_get_line(matrix, i):
	_check_matindex(matrix,i,0)
	im, jm = matrix_size(matrix)
	line = []
	for n in range(jm):
		line.append(matrix_get(matrix, i, n))
	return line
	
def matrix_set_line(matrix, i, val):
	_check_matindex(matrix,i,0)
	im, jm = matrix_size(matrix)
	for n in range(jm):
		matrix_set(matrix, i, n, val)


def matrix_get_col(matrix, j):
	_check_matindex(matrix,0,j)
	im, jm = matrix_size(matrix)
	col = []
	for n in range(im):
		col.append(matrix_get(matrix, n, j))
	return col
	
def matrix_set_col(matrix, j, val):
	_check_matindex(matrix,0,j)
	im, jm = matrix_size(matrix)
	for n in range(im):
		matrix_set(matrix, n, j, val)
	
	
	
if __name__ == '__main__':
	m = matrix_maker(5, 3)
	matrix_set(m,0, 0, 1)
	matrix_set(m,0, 2, 2)
	matrix_set(m,4, 0, 12)
	matrix_set(m,4, 2, 15)
	matrix_print(m)
	print "get line 0",  matrix_get_line(m, 0)
	print "get col 0", matrix_get_col(m, 0)
	
