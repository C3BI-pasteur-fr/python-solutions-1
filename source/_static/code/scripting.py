from subprocess import Popen, PIPE

   
cmd = 'clustalw -align -infile={0} -output=FASTA -outfile=alignement.fa'.format('../data/abcd.fasta')
clustal_process = Popen(cmd, shell = True, stdout = PIPE, stderr = PIPE)
stdout, stderr = clustal_process.communicate()

return_code = clustal_process.poll()
if return_code != 0 :
    raise RuntimeError("something goes wrong with clustalw :"+stderr)