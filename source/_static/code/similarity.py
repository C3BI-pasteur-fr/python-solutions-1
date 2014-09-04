from matrix import *

lines = iter( ['  A G C U\n',
               'A 1.0 0.5 0.0 0.0\n',
               'G 0.5 1.0 0.0 0.0\n',
               'C 0.0 0.0 1.0 0.5\n',
               'U 0.0 0.0 0.5 1.0\n']
             )

def parse_similarity_file():
    """
    parse file containing RNA similarity matrix and return a matrix
    """
    sim_matrix = matrix_maker(4, 4)
    #skip first line
    lines.next()
    for row_no, line in enumerate(lines):
        line = line.strip()
        fields = line.split()
        values = [float(val) for val in fields[1:]]
        matrix_replace_row(sim_matrix, row_no, values)
    return sim_matrix

def get_similarity(b1, b2, sim_matrix):
    """
    :param b1: the first base must be in ('A', 'G', 'C', 'U')
    :type b1: string
    :param b2: the first base must be in ('A', 'G', 'C', 'U')
    :type b2: string
    :param sim_matrix: a similarity matrix
    :type sim_matrix: matrix
    :return: the similarity between b1 and b2
    :rtype: float
    """
    bases = {'A':0 , 'G':1, 'C':2, 'U':3}
    b1 = b1.upper()
    b2 = b2.upper()
    if not b1 in bases:
        raise KeyError("unknown base b1: " + str(b1))
    if not b2 in bases:
        raise KeyError("unknown base b2: " + str(b2))
    return matrix_get_cell(sim_matrix, bases[b1], bases[b2])
                           
def compute_similarity(seq1, seq2, sim_matrix):
    """
    compute a similarity score between 2 RNA sequence of same lenght
    :param seq1: first sequence to compare
    :type seq1: string
    :param seq2: second sequence to compare
    :type seq2: string
    :param sim_matrix: the similarity between b1 and b2
    :type sim_matrix: matrix
    :return: the similarity score between seq1 and seq2
    :rtype: float
    """
    similarities = []
    for b1, b2 in zip(seq1, seq2):
        sim = get_similarity(b1, b2, sim_matrix)
        similarities.append(sim)
    return sum(similarities)
            
if __name__ == '__main__':
    seq1 = 'AGCAUCUA'
    seq2 = 'ACCGUUCU'
    sim_matrix = parse_similarity_file()
    print matrix_to_str(sim_matrix)
    similarity = compute_similarity(seq1, seq2, sim_matrix)
    print similarity
            