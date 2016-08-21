#!/usr/bin/python
import sys

try:
    file_r = open(sys.argv[1],"r")
    #file_r = open('input_pancake',"r")
    items = file_r.readlines()
except:
    print '\nCannot open input file\n'
    exit(1) 

try:
    #file_w = open('output_pancake',"w")
    file_w = open(sys.argv[2],"w")
except:
    print '\nCannot open input file\n'
    exit(1) 

for i in xrange(0,len(items)):
    try:
        items[i] = items[i].split('\n')[0]
    except:
        print '\nMaybe the last one\n'

def invert(vector,end):
    part = []
    for i in xrange(0,end):
        part.append('+' if vector[i]=='-' else '-')
    for i in xrange(0,end):
        vector[i]=part[end-i-1]


for j in xrange(1,int(items[0])+1):
    full = list(items[j])
    flips = 0
    pos = len(full)-1
    print j
    print full
    while (pos>-1):
        if full[pos]=='-':
            if full[0]=='-':
                invert(full,pos+1)
                flips+=1
                print flips,pos,full
            else:
                start = 0
                while full[start]=='+':
                    start+=1
                invert(full,start)
                flips+=1
                print flips,pos,full
        else:
            pos-=1
        
    print flips, full
    file_w.write('Case #{0}: {1}\n'.format(j,flips))

file_w.close()
