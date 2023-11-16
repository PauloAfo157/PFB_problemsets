#!/usr/bin/env python3

genes= {}
seqName = ''
seq = ''
seq_id= ''

with open('Python_08.fasta', 'r') as f:
    for l in f:
        if l.startswith('>'):
            if len(seqName) > 0:
                genes[seq_id] = { 'sequence' : seqName , 'description' : seq }
                seqName = ''

            l = l.lstrip('>')
            l = l.rstrip()

            seq_id, seq = l.split(maxsplit = 1)

        else:
            seqName += l.rstrip()

    if len(seqName) > 0:
        genes[seq_id] = { 'sequence' : seqName , 'description' : seq }
with open('Python_08.codons-frame-1.nt', 'w') as w:        
    for k in genes:
        split_seq =''
        seq_splited = genes.get(k).get('sequence')
        for j in [0,1,2]:
            split_seq = ''
            for i in range(j, len(seq_splited), 3):
                split_seq += seq_splited[i:i+3] + ' '
                w.write(k+'-'+'frame '+str(1+j)+'-codons'+'\n'+split_seq+'\n')
        for i in range(0, len(seq_splited),3):
            split_seq += seq_splited[i:i+3] + ' '
            w.write(k+'-'+'frame 1 codons'+'\n'+split_seq+'\n')





