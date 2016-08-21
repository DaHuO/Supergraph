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




def check_ticks(NUM, TICKS):
    X = NUM
    while X >= 10:
        TICKS[int(X%10)] = 1
        X = X/10
        if DEBUG:
            print X
    TICKS[X] = 1

    return TICKS




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

            if int(L[0]) == 0:
                print "INSOMNIA"
                solution = "INSOMNIA"
            else:
                TICKS = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                DONE = False
                N = int(L[0])
                i_N = 0
                while not DONE:
                    i_N = i_N+1
                    TICKS = check_ticks(i_N*N, TICKS)

                    if sum(TICKS) == 10:
                        DONE = True
                solution = i_N*N

            f_out.write("Case #{}: {}\n".format(c[0], solution))
