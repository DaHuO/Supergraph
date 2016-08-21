#!/usr/bin/env python
# Edward Lau
# 20150410





###############
## VARIABLES ##
###############
import numpy
IN_FILE="./sampleIn"
IN_FILE="./B-large.in"
OUT_FILE="./sampleOut"
OUT_FILE="./B-large.out"
N_SKIP=0
CASES = list()
N_C=0
i_C=0
DEBUG = False
#DEBUG = True





##################
## READ IN FILE ##
##################
with open(IN_FILE, 'r') as f_in:

    ####################
    ## WRITE OUT FILE ##
    ####################
    with open(OUT_FILE, 'w') as f_out:

        ##############
        ## DO STUFF ##
        ##############
        N_C = int(f_in.readline())

        while i_C < N_C:
            i_C += 1
            solution = 0

            L = f_in.readline().split()
            if DEBUG:
                print L

            c = list()
            c.append(i_C)
            c.append(L)
            CASES.append(c)

            L2 = [0]*(len(L[0])+1)
            for index, pancake in enumerate(L[0]):
                if pancake == "+":
                    L2[index] = 1
                elif pancake == "-":
                    L2[index] = -1

            if DEBUG:
                print L2

            L2[len(L[0])] = 1

            L3 = numpy.diff(L2).nonzero()
            if DEBUG:
                print len(L3[0])
            solution = len(L3[0])
            f_out.write("Case #{}: {}\n".format(c[0], solution))
