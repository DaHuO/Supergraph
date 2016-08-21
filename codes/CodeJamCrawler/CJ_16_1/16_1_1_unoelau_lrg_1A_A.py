#!/usr/bin/env python
# Edward Lau
# 20150410





###############
## VARIABLES ##
###############
IN_FILE="./sampleIn"
IN_FILE="./A-large.in"
OUT_FILE="./sampleOut"
OUT_FILE="./A-large.out"
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

            BESTWORD = list()
            FIRST = True
            for i_L in L[0]:
                if DEBUG:
                    print i_L
                    print BESTWORD

                if FIRST:
                    BESTWORD.append(i_L)
                    FIRST = False
                elif i_L >= BESTWORD[0]:
                    BESTWORD.insert(0, i_L)
                else:
                    BESTWORD.append(i_L)

            if DEBUG:
                print ''.join(BESTWORD)
            solution = ''.join(BESTWORD)

            f_out.write("Case #{}: {}\n".format(c[0], solution))
