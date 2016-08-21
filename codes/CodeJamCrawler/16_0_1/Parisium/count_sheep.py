#!/usr/bin/env python

# number of test cases
T = int(raw_input())

# loop through ever line
for i in range(1, T+1):
    # starting number
    N = int(raw_input())

    # check special case
    if N == 0:
        print "Case #%d: INSOMNIA" %(i)

    else:
        # master list to store the 10 digits
        M = list(set(map(int,str(N))))
        # sleep status
        sleep = False

        # initialize multiplier
        x = 2

        # start counting
        while sleep == False:
            # next number
            N_o = x * N

            # parse into individial digits
            temp = map(int,str(N_o))

            # compare to master to find new and unique digits
            diff = list(set(temp) - set(M))

            # add the new digits to the master list
            M.extend(diff)

            # sort the master list
            M.sort()

            # increment multiplier
            x = x + 1

            # if M == [0,1,2,3,4,5,6,7,8,9]:
            if len(M) == 10 and M == [0,1,2,3,4,5,6,7,8,9] :
                sleep = True
                print "Case #%d: %d" %(i, N_o)
            # end if
        # end while
    # end else
# end for loop

# end of file
