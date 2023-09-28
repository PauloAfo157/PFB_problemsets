#!/usr/bin/env python3

import sys

number1=int(sys.argv[1])
number2=int(sys.argv[2])

if number1 % 2 == 0:
    print(number1,'is even')
else:
    print(number1, 'is odd, add an even number')
if number2 % 2 == 0:
    print(number2, 'is even')
else:
    print(number2, 'is odd, add an even number')

while number1 and number2 % 2 == 0:
    print(number1)
    number1+=1
    if number1 == number2+1:
        print('Done')
        break

        
