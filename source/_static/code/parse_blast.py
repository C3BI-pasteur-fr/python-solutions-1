from operator import itemgetter
from collections import namedtuple

Hit = namedtuple("Hit" ,"id percent identity align_len mis_num, open_gap_num\
                  query_start, query_end, subject_start, subject_end, E_value, HSP_bit_score")

def parse_blast_output(input_file):
    """
    :param input_file: the path of the blast report (in m8 format) to parse
    :type input_file: string
    :return: list of hits
    :rtype: list of Hit
    """
    with open(input_file, 'r') as infile:
        table = []
        for line in infile:
            col = line.split('\t')
            try:
                col[2] = float(col[2])
            except ValueError as err:
                raise RuntimeError("error in parsing {} : {}".format(input_file, err))
            col[-1] = col[-1][:-1]
            table.append(col)
    return table


def write_blast_output(hits, output_file):
    """
    Write hits in file in format text
    one hit per line
    
    :param hits: hit to wite in file
    :type hits: namedtuple Hit
    :param output_file: the path of the file to write hits in
    :type output_file: string
    """
    with open(output_file, 'w') as output:
        for row in table_sorted:
            row = [str(x) for x in row]
            output.write("\t".join(row) + "\n")

   
if __name__ == '__main__':
    table_hits = parse_blast_output('blast2.txt')
    #table_hits = parse_blast_output('blast.txt')
    table_sorted = sorted(table_hits, key = itemgetter(2), reverse = True)
    # alternative
    # table_sorted = sorted(table, key = lambda x : x[2], reversed = True)
    write_blast_output(table_hits, 'blast_sorted.txt')  
   
         
