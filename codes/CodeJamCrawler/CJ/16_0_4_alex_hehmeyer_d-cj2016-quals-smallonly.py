########################################################
# FRACTILES - Google Code Jam 2016 Quals
# Problem D
########################################################

import time
import math

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
    K, C, S = map(int, input().split(' '))


    # Echo the inputs for debugging
    if SHOW_DEBUG:
        print('\nCASE #' + str(casesdone))

    #####################
    # Start Solution Here
    #####################

    # If S == K, then this is easy - jsut print out positions 1 to K
    pos_needed = int(math.ceil(K/C))
    if pos_needed > S:
        answer = 'IMPOSSIBLE'
    else:
        answerlist = [i+1 for i in range(K)]
        answer = ''
        for item in answerlist:
            answer += str(item) + ' '
        answer.strip()

    
    #############################
    # Solve and print the answer!
    #############################
    print('Case #' + str(casesdone) + ': ' + answer)





    #############################
    # Some code to print out the script's performance, if that option is enabled
    if SHOW_PERF_TIMES and casesdone % 10 == 0:
        stop = time.clock()
        print('TIME:  Cases ' + str(casesdone-10) + ' to ' + str(casesdone) + ' TOTAL: ' + str(stop-start) + ' AVG: ' + str((stop-start)/10))
        start = time.clock()

veryend = time.clock()
if SHOW_PERF_TIMES:
    print('\nTIME:  Total Program Time: ' + str(veryend-verystart))
