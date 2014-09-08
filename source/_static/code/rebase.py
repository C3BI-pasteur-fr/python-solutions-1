
def rebase_parser(rebase_file):
    """
    :param rebase_file: the rebase file to parse
    :type rebase_file: file object
    :return: at each call return a tuple (str enz name, str binding site)
    :rtype: iterator
    """
    def clean_seq(seq):
        """
        remove each characters which are not a base
        """
        clean_seq = ''
        for char in seq:
            if char in 'ACGT':
                clean_seq += char
        return clean_seq
    
    for line in rebase_file:
        fields = line.split()
        #fields = fields.split()
        name = fields[0]
        seq = clean_seq(fields[2])
        yield (name, seq)
     
        
if __name__ == '__main__':
    import sys
    import os.path
    
    if len(sys.argv) != 2:
        sys.exit("usage multiple_fasta fasta_path")
    rebase_path = sys.argv[1]
    if not os.path.exists(rebase_path):
        sys.exit("No such file: {}".format(rebase_path))
        
    with open(rebase_path, 'r') as rebase_input:   
        for enz in rebase_parser(rebase_input):
            print enz   