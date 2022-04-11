import sys
from Bio import SeqIO

def read_set(filename):
    s = set()
    with open(filename) as h:
        for line in h:
            s.add(line.rstrip())
    return s


to_be_extracted = read_set(sys.argv[2])

for seq in SeqIO.parse(sys.argv[1], "fasta"):
    if seq.id in to_be_extracted:
        print(seq.format("fasta"))
