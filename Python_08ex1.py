#!/usr/bin/env python3

genes= {}
seqName = ''
seq = ''
seq_id = ''

with open('Python_08.fasta', 'r') as f:
    for l in f:
        if l.startswith('>'):
            genes[seq_id] = { 'sequence' : seqName , 'description' : seq}
            seqName = ''
            l = l.rstrip('>')
            l = l.rstrip().upper()
            seq_id, seq = l.split(maxsplit = 1)

        else:
            seqName += l.rstrip()

    for key in genes:
        seq_c= genes.get(key).get('sequence')
        cA = seq_c.count('A')
        cT = seq_c.count('T')
        cC = seq_c.count('C')
        cG = seq_c.count('G')


        print("seqName\tA_count\tT_count\tG_count\tC_count")
        print(key+'\t'+str(cA)+'\t'+str(cT)+'\t'+str(cG)+'\t'+str(cC))
        

