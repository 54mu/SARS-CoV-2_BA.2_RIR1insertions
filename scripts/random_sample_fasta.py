from tqdm import tqdm
import sys 
from Bio import SeqIO
import random as rnd
import re

## samples p sequences from a fasta file. 
## this requires pre-counting the sequences
## storing them in a list or tuple may be faster
## but may require too much memory
## so for now reads the file twice

p = int(sys.argv[2])

counter = 0


pattern = '>'
with open(sys.argv[1]) as fasta:
    counter = len(re.findall(pattern, fasta.read()))

'''
for seq in SeqIO.parse(sys.argv[1], "fasta"):
    counter +=1
'''

samples = set(rnd.sample(range(0,counter), p))
last = sorted(list(samples))[-1]

c = 0

for seq in SeqIO.parse(sys.argv[1], "fasta"):
    if c > last:
        break
    if c in samples:
        print(seq.format("fasta"), end = '')
    c += 1

