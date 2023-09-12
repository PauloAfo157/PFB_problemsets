#!/usr/bin/env python3

dna = 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA'

if 'ATG' in dna:
    print('found ATG in your dna sequence')
elif 'TTT' in dna:
    print('found TTT in your dna sequence')
else:
    print('did not find ATG in your dna sequence')


