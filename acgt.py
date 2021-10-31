import random
i = 0
print("input length of sequence")
length = int(input())
seq=[]
sum = 0
beg = 0
dict = {1: 'A', 2: 'C', 3: 'G', 4:'T'}
gencode = { 'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
    'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W' }
    
while (i != length):
    val = random.randint(1,4)
    seq.append(val)
    i += 1
i = 0
for nuc in seq:
    seq[i] = dict[nuc]
    i += 1
i = 0
j = 0
seq = ''.join(seq)
aminoseq = ''
while(i + 3 <= length):
    dkey = seq[i:i+3]
    if (len(dkey) != 3):#add check
        break
    aminoseq += gencode[dkey]
    if (aminoseq[-1] == '*'):
        j = aminoseq.find('*')
        print (aminoseq[0:j])
        i += 1
        continue
    i += 3
print(seq)
print("aminoseq is:")
print(aminoseq)