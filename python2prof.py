#!/usr/bin/env python3

import sys

input=int(sys.argv[1])
print(type(input))
print(input)

if input < 0:
    print('o número é negativo')
elif input > 0:
    print('o número é positivo')
    if input < 50:
        print('número menor que 50')
        if input %2 == 0:
            print('its an even number that is smaller than 50')
    else:
        print('número maior que 50')
        if input%3 == 0:
            print('número maior que 50 e divisível por 3')
else:
    print('o número deve ser 0')



