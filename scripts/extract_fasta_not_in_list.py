import sys
from Bio import SeqIO

def read_list(filename):
    rset = set()
    with open(filename) as handle:
        for line in handle:
            rset.add(line.rstrip())
    return rset

exclusion_set = read_list(sys.argv[2])

for seq in SeqIO.parse(sys.argv[1], "fasta"):
    if seq.id not in exclusion_set:
        print(seq.format("fasta"))
