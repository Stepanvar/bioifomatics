#!/bin/bash
FASTA_FILE = $1
FASTA_QUERY = $2
for var in $(FASTA_FILE)
do
	blastn -query $(FASTA_QUERY) -subject $var -task blastn -word_size 11 -max_hsps 1 -max_target_seqs 1400 -outfmt "6 qaccver saccver length qstart sstart qend send mismatch gapopen evalue bitscore" >> $(FASTA_FILE)_res.txt 
done
