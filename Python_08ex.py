#!/usr/bin/env python3
genes= {}
seq_id = '' 
with open('Python_08.fasta', 'r') as seq_read:
    for l in seq_read:
        l = l.rstrip()
        if l.startswith('>'):
            seqName = l.lstrip('>').split(' ', maxsplit=1)
            seq_id = seqName[0]
            genes[seq_id] = {
                    'A': 0, 'T': 0, 'G': 0, 'C': 0}    
        else:
            for n in l:
                genes[seq_id][nucleotide] += 1
                print(genes)

    print("seqName\tA_count\tT_count\tG_count\tC_count")

    for seq_id in genes:
        print('\t'.join((seq_id,
        str(genes[seq_id]['A']),
        str(genes[seq_id]['C']),
        str(genes[seq_id]['G']),
        str(genes[seq_id]['T'])
    )))
