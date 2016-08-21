__author__ = 'hannahkim'

import sys
import numpy as np

N = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
count = dict()
for i in range(0,len(N)):
    thisnum = N[i]
    for j in range(0,len(thisnum)):
        letter = thisnum[j]
        try:
            count[letter] += 1
        except KeyError:
            count[letter] = 1
print count

input_file = sys.argv[1]
output_file = 'out_'+input_file
inputf = open(input_file,'r')
output = open(output_file, 'w')
n = int(inputf.readline())
print n
for i in range(1,n+1):
    thisnum = inputf.readline().rstrip('\n')
    fin = ''
    input = dict()
    for j in range(0,len(thisnum)):
        letter = thisnum[j]
        try:
            input[letter] += 1
        except KeyError:
            input[letter] = 1
    # print input
    if input.has_key('Z') and input['Z']>0:
            a = input['Z']
            for k in 'ZERO':
                input[k] -= a
            fin += '0'*a
    # print input
    if input.has_key('W') and input['W']>0:
        a = input['W']
        for k in 'TWO':
            input[k] -= a
        fin += '2'*a
    # print input
    if input.has_key('U') and input['U']>0:
        a = input['U']
        for k in 'FOUR':
            input[k] -= a
        fin += '4'*a
    # print input
    if input.has_key('X') and input['X']>0:
        a = input['X']
        for k in 'SIX':
            input[k] -= a
        fin += '6'*a
    # print input
    if input.has_key('G') and input['G']>0:
        a = input['G']
        for k in 'EIGHT':
            input[k] -= a
        fin += '8'*a
    # print input
    if input.has_key('H') and input['H']>0:
        a = input['H']
        for k in 'THREE':
            input[k] -= a
        fin += '3'*a
    if input.has_key('F') and input['F']>0:
        a = input['F']
        for k in 'FIVE':
            input[k] -= a
        fin += '5'*a
    if input.has_key('V') and input['V']>0:
        a = input['V']
        for k in 'SEVEN':
            input[k] -= a
        fin += '7'*a
    if input.has_key('I') and input['I']>0:
        a = input['I']
        for k in 'NINE':
            input[k] -= a
        fin += '9'*a
    if input.has_key('O') and input['O']>0:
        a = input['O']
        for k in 'ONE':
            input[k] -= a
        fin += '1'*a
    output.write('CASE #'+str(i)+': '+(''.join(sorted(fin)))+'\n')
    print 'CASE #'+str(i)+': '+(''.join(sorted(fin)))
inputf.close()
output.close()