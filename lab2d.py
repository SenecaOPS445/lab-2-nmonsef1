#!/usr/bin/env python3


import sys

#Check if not exactly 2 arguments input (including sys.argv[0], so !=3)
if len(sys.argv) !=3:
    print('Usage: ./lab2d.py name age')
    sys.exit()

#Assign the command line arguument to name and ages variables
name = sys.argv[1]
age = sys.argv[2]


#Print the message including name and age
print('Hi ' + name + ', you are ' + age + ' years old.') 