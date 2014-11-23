import sys
import os.path

sys.path.insert(0, os.path.join(expanduser('~'), "my_python_lib"))

import matrix


def parse_similarity_file(path):
    """
    parse file containing RNA similarity matrix and return a matrix
    """
    sim_matrix = matrix.create(4, 4)
    with open(path, 'r') as sim_file:
        #skip first line
        sim_file.next()
        for row_no, line in enumerate(sim_file):
            line = line.strip()
            fields = line.split()
            values = [float(val) for val in fields[1:]]
            matrix.replace_row(sim_matrix, row_no, values)
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
    return matrix.get_cell(sim_matrix, bases[b1], bases[b2])
                      
                           
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
    sim_matrix = parse_similarity_file("similarity_matrix")
    print matrix.to_str(sim_matrix)
    similarity = compute_similarity(seq1, seq2, sim_matrix)
    print similarity
            
