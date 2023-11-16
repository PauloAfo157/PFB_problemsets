#!/usr/bin/env python3

import re

genes= {}
codons_frames={}

with open('Python_08.fasta', 'r') as f:
    for l in f:
        if l.startswith('>'):
            l_juntas = ''
            geneID = re.search(r'>([\w]{8,10})', l).group(1)

            l = l.lstrip('>')
            l = l.rstrip()

        else:
            l_juntas += l.strip()
            genes[geneID] = ''.join(l_juntas)

for geneID in genes:
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

with open('Python_08.codons-frame6.nt','w') as w:
    for geneID in codons_frames:
        for frame in codons_frames[geneID]:
            headline = geneID + '_' + frame + '\n'
            w.write(headline)
            codons = ' '.join(codons_frames[geneID][frame]) + '\n'
            w.write(codons)






