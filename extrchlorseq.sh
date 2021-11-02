LIST=$1
for eachfile in $(cat $LIST)
do
cat ${eachfile}_blast| sort -nk 6,6 | awk -F "\t" '$6 >=2000'| awk '!seen[$1]++' > sort_${eachfile}_blast
cat sort_${eachfile}_blast | cut -f1 > nodeid.txt
bioawk -cfastx 'BEGIN{while((getline k <"nodeid.txt")>0)i[k]=1} {if(i[$name])print ">"$name"\n"$seq}' ${eachfile}.fasta > chlor_seq_${eachfile}.fasta
mv sort_${eachfile}_blast -t ${eachfile}
mv nodeid.txt -t ${eachfile}
mv chlor_seq_${eachfile}.fasta -t ${eachfile}
done