#name of fasta or fastq file which need filt
NAMEF=$1 
#by what filt: length, cov, node with sign
FILTRN=$2
#filtering number
NUMB=$3

seqkit fx2tab ${NAMEF}.fastq |csvtk mutate -H -t -f 1 -p "${FILTRN}.([0-9]+)"| awk -F "\t" '$4 >='$NUMB| seqkit tab2fx >> "${NAMEF}_seqkit_$FILTRN$NUMB.fastq"