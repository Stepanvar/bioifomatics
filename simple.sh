#!/bin/bash
awk 'BEGIN{RS = ">"; i = 1} {if ($0) {print ">"$0 > "seq_"i".fasta"; i++}}' mt_dna.fasta
for pat in seq_*.fasta
do
	head -1 $pat | grep -v $(head -1 $pat) $pat > unhead_$pat
done
