#!/usr/bin/env python3

import re

genes= {}
codons_frames={}
protein_frames = {}
translation_table = {
    'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
    'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R',
    'AAT':'N', 'AAC':'N',
    'GAT':'D', 'GAC':'D',
    'TGT':'C', 'TGC':'C',
    'CAA':'Q', 'CAG':'Q',
    'GAA':'E', 'GAG':'E',
    'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',
    'CAT':'H', 'CAC':'H',
    'ATT':'I', 'ATC':'I', 'ATA':'I',
    'TTA':'L', 'TTG':'L', 'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L',
    'AAA':'K', 'AAG':'K',
    'ATG':'M',
    'TTT':'F', 'TTC':'F',
    'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
    'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S', 'AGT':'S', 'AGC':'S',
    'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
    'TGG':'W',
    'TAT':'Y', 'TAC':'Y',
    'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',
    'TAA':'*', 'TGA':'*', 'TAG':'*'
}

with open('Python_08.fasta', 'r') as f:
    for l in f:
        if l.startswith('>'):
            l_juntas = ''
            geneID = re.search(r'^>([\w]{8,10})', l).group(1)

            l = l.lstrip('>')
            l = l.rstrip()

        else:
            l_juntas += l.strip()
            genes[geneID] = ''.join(l_juntas)

for geneID in genes.keys():
        rvgenes = genes[geneID][::-1]
        rvgenes.replace('A','t').replace('T','a').replace('C','g').replace('G','c')
        rvgenes = rvgenes.upper()
        codons_frames[geneID] = {}
        for frame in range(3):
            codons = re.findall(r'.{3}', genes[geneID][frame:])
            frameID = 'frame_+' + str(frame+1)
            codons_frames[geneID][frameID] = codons
            codonsrv = re.findall(r'.{3}', rvgenes[frame:])
            frameIDrv = 'frame_-'+ str(frame +1)
            codons_frames[geneID][frameIDrv] = codonsrv

for geneID in codons_frames.keys():
    protein_frames[geneID] = codons_frames
    for frame in codons_frames[geneID]:
        protein =''
        for codon in codons_frames[geneID][frame]:
            if codon in translation_table:
                protein += translation_table[codon]
            else:
                print('codon não está presente no dicionário de tradução')
                exit()
        protein_frames[geneID][frame] = protein

with open('Python_08.translated-longest.aa','w') as w:
    for geneID in protein_frames.keys():
        longestprotein = ''
        longestframe = ''
        for frame in protein_frames[geneID]:
            proteins = re.findall(r'(M[A-Z]+?)\*', protein_frames[geneID][frame])
            for i in proteins:
                if len(i.group(1)) > len(longestprotein):
                    longestprotein = i.group(1)
                    longestframe = frame
                    posstart = i.start(1)
                    posend = i.end(1)
                    longestcodon = codons_frames[geneID][frame][posstart:posend]
            
            result = geneID +'\t'+frame+'\n'+longestcodon+'\n'+longestprotein
            w.write(result)




