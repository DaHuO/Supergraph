import os
import math
#from datetime import datetime
#start_time = datetime.now()

case_num = 1
#if S = K, then you can simply check the first S tiles, which will either equal the original sequence
#or = GGG...GGG S times. The only way to get all L's in the first S tiles is if the original sequence
#was all L's.
#def all_possibilities(tiles, complexity):
    
def printout_order(x):
    string = ''
    for i in range(1, x + 1):
        string += ' %s' % str(i)
    return string

with open('D-small-attempt0.in', 'rb') as text_file:
    t = text_file.readline().strip('\r\n')
    for line in text_file:
        line = line.strip('\r\n').split()
        K = int(line[0])
        C = int(line[1])
        S = int(line[2])
        print 'Case #%s:%s' % (case_num, printout_order(S))
        case_num += 1

#print datetime.now() - start_time
