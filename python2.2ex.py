#!/usr/bin/env python3

import sys

input=int(sys.argv[1])
print(type(input))
print(input)

if input %4 == 0:
    if input %100 == 0:
        if input %400 == 0:
            print('Bissexto')
        else:
            print('Não')
    else:
        print('Bissexto')
else:
    print('Não')

