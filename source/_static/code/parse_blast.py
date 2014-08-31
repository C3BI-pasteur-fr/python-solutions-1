from operator import itemgetter

def parse_blast_output(input_file, output_file):
   with open(input_file, 'r') as infile:
      table = []
      for line in infile:
         print i 
         col = line.split('\t')
         try:
            col[2] = float(col[2])
         except ValueError as err:
            raise RuntimeError("error in parsing {} : {}".format(input_file, err))
         col[-1] = col[-1][:-1]
         table.append(col)
   #from this point the input_file is closed
   table_sorted = sorted(table, key = itemgetter(2), reverse = True)
   # alternative
   # table_sorted = sorted(table, key = lambda x : x[2], reversed = True)
   with open(output_file, 'w') as output:
      for row in table_sorted:
         row = [str(x) for x in row]
         output.write("\t".join(row) + "\n")
         
