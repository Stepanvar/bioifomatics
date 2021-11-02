list=$1
mkdir trimmed
for eachfile in $(cat $list)
do 
 trimmomatic SE ${eachfile}.fastq ${eachfile}_tr11_hcr4.fastq ILLUMINACLIP:/export/home/user/miniconda3/envs/bioinfo/share/trimmomatic-0.39-1/adapters/TruSeq3-PE-2.fa:2:30:10 TRAILING:11 HEADCROP:4 MAXINFO:247:0.6 MINLEN:100
 mv ${eachfile}_tr11_hcr4_maxin24706_min100.fastq -t trimmed
done


