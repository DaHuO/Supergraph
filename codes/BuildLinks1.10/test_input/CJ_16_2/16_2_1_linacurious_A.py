attempt_list = ['A-test','A-small-attempt0','A-large']
attempt = attempt_list[2]

import time
time.clock()

from collections import Counter

def solve(s):
    c = Counter(s)
    t = [0] * 10
    t[0] = c['Z'] # Z = that many ZEROs
    t[2] = c['W'] # W = that many TWOs
    t[4] = c['U'] # U = that many FOURs
    t[6] = c['X'] # X = that many SIXs
    t[8] = c['G'] # G = that many EIGHTs
    t[5] = c['F'] - t[4] # F = that many FIVEs (- 1x FOURs)
    t[7] = c['S'] - t[6] # S = that many SEVENS (- 1x SIXs)
    t[3] = c['H'] - t[8] # H = that many THREEs (- 1x EIGHTs)
    t[9] = c['I'] - t[8] - t[6] - t[5] # I = that many NINEs (- 1x EIGHTs - 1x SIXs - 1x FIVEs)
    t[1] = c['O'] - t[0] - t[2] - t[4] # O = that many ONEs (- 1x ZEROs - 1x TWOs - 1x FOURs)
    return '0'*t[0]+'1'*t[1]+'2'*t[2]+'3'*t[3]+'4'*t[4]+'5'*t[5]+'6'*t[6]+'7'*t[7]+'8'*t[8]+'9'*t[9]

def main():
    fin = open(attempt + '.in', 'r')
    fout = open(attempt + '.out','w')

    numcases = int(fin.readline())

    for casenum in range(1,numcases+1):
        s = fin.readline()
        fout.write('Case #' + repr(casenum) + ': ' + str(solve(s)) + '\n')

    fin.close()
    fout.close()

main()
print(time.clock())