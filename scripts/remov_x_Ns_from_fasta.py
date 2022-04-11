import sys
from Bio import SeqIO

seqfile = sys.argv[1]
n = int(sys.argv[2])

filter_string = "n" * n

for seq in SeqIO.parse(seqfile, "fasta"):
    if filter_string not in str(seq.seq).lower():
        print(seq.format("fasta"))


