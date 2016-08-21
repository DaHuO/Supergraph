#!/usr/bin/python3

import getopt
import sys
import math

if __name__ == "__main__":

    verbose = False
    fname = "input.txt"

    if sys.version_info[0] < 3:
        print("This script requires Python 3. (You are running %d.%d)" % (
            sys.version_info[0], sys.version_info[1])) 
        sys.exit()

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hvf:",
                                   ["verbose","help","input="])
    except getopt.GetoptError as err:
        print (str(err)) 
        sys.exit(2)

    for o, a in opts:
        if o in ("-h", "--help"): sys.exit()
        elif o in ("-v", "--verbose"): verbose = True
        elif o in ("-f", "--input"): fname = a
        else: sys.exit()

    f = open(fname, "rt")
    ncases = int(f.readline())

    for c in range(ncases):
        N = int(f.readline())
        seen = [0 for x in range(10)]
        all_seen = False

        if verbose:
            print("%d: N == %d" % (c+1,N))
        
        if N == 0:
            print("Case #%d: %s" % (c+1,"INSOMNIA"))
            continue
        
        attempts = 0
        cN = 0
        while(not all_seen):
            attempts += 1
            cN = N * attempts

            if verbose:
                print("%d - cN = %d" % (attempts, cN))
            
            # look at cN
            while(cN):
                digit = cN % 10
                seen[digit] += 1
                cN //= 10

            if not(0 in seen):
                all_seen = True

            if verbose:
                print(seen)
                
        print("Case #%d: %d" % (c+1,N*attempts))

            
        
        






        

        




