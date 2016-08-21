########################################################
# SENATE EVACUATION - Google Code Jam 2016 Round 1C
# Problem A
########################################################

import time

#########################
# GLOBAL VARIABLES
# A few global variables
#########################
# User Controlled Global Variables
SHOW_PERF_TIMES = False
SHOW_DEBUG = False

# Other Global Variables


#####################################################
# FUNCTIONS
# This section contains any necessary functions
#####################################################








#####################################################
# MAIN PROGRAM
#####################################################

verystart = time.clock()

# Read number of test cases
testcase_count = int(input())
casesdone = 0

# Main loop
start = time.clock()
while casesdone < testcase_count:
    casesdone += 1
    
    # Read the inputs for this test case here
    N = int(input())
    senators = list(map(int, input().split(' ')))

    # Echo the inputs for debugging
    if SHOW_DEBUG:
        print('\nCASE #' + str(casesdone) + ' N: ' + str(N) + ' Senators: ' + str(senators))

    #####################
    # Start Solution Here
    #####################

    evacplan = ''
    senate_count = sum(senators)
    numparties = len(senators)
    partiesleft = numparties

    
    while senate_count > 0:
        maxparty = 0
        partiesleft = 0
        for partycount in senators:
            if partycount > 0:
                partiesleft += 1
            if partycount > maxparty:
                maxparty = partycount

        if partiesleft == 2:
            for i in range(numparties):
                partycount = senators[i]
                if partycount == maxparty:
                    senators[i] -= 1
                    senate_count -= 1
                    evacplan += chr(ord('A')+i)
        else:
            for i in range(numparties):
                partycount = senators[i]
                if partycount == maxparty:
                    senators[i] -= 1
                    senate_count -= 1
                    evacplan += chr(ord('A')+i)
                    break

        if senate_count > 0:
            evacplan += ' '
        



    #############################
    # Solve and print the answer!
    #############################
    print('Case #' + str(casesdone) + ': ' + evacplan)





    #############################
    # Some code to print out the script's performance, if that option is enabled
    if SHOW_PERF_TIMES and casesdone % 10 == 0:
        stop = time.clock()
        print('TIME:  Cases ' + str(casesdone-10) + ' to ' + str(casesdone) + ' TOTAL: ' + str(stop-start) + ' AVG: ' + str((stop-start)/10))
        start = time.clock()

veryend = time.clock()
if SHOW_PERF_TIMES:
    print('\nTIME:  Total Program Time: ' + str(veryend-verystart))
