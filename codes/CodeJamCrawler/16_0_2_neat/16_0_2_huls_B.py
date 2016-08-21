#!/usr/bin/python


from __builtin__ import list


import sys, os, time,  string

'''
  Code jam 2016 - huls
'''

INPUT_FILE = "c:\\cj2016\\B-small-attempt0.in"
OUTPUT_FILE = "c:\\cj2016\\B-small-attempt0.out"
'''
INPUT_FILE = "c:\\cj2016\\B.in"
OUTPUT_FILE = "c:\\cj2016\\B.out"
'''
f_in = open(INPUT_FILE, 'r')
f_out = open(OUTPUT_FILE, 'w')



def solve():
    pencakes = list(f_in.readline().rstrip('\n'))
    numberOfFlips = 0
    flipNeeded = False
    for i in range(len(pencakes)-1, -1 , -1):
        if( (pencakes[i] == '+') and ( flipNeeded == False ) ): 
            continue
        if( (pencakes[i] == '+') and flipNeeded ):
            for j in range(0, i+1 ) :
                if (pencakes[j] == '-') :
                    pencakes[j] = '+'
                else:
                    pencakes[j] = '-'
            numberOfFlips = numberOfFlips + 1
            flipNeeded = False
        if( (pencakes[i] == '-') and ( flipNeeded == False ) ):
            flipNeeded = True
    if(flipNeeded):
        numberOfFlips = numberOfFlips + 1
    return numberOfFlips
    
def main():
    T = int(f_in.readline())
    for case in range(1, T+1):
        print case
        sol = solve()
        f_out.write("Case #" + str(case) + ": " + str(sol) + "\n")
    print "Finished"
    
if __name__ == "__main__":
    startTime = time.clock()
    main()
    print "Completed in {} seconds. \n" . format(time.clock() - startTime)