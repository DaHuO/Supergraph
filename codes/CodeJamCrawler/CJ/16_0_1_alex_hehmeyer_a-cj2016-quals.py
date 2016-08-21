########################################################
# COUNTING SHEEP - Google Code Jam 2016 Quals
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


# Returns a number where, when interpreted in binary
# if a given position in the number is 1, then that
# digit has been found
def checkDigits(n):
    digitPresent = 0
    for digit in str(n):
        digit = int(digit)
        digitPresent = digitPresent | (1 << digit)
    return digitPresent


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


    # Echo the inputs for debugging
    if SHOW_DEBUG:
        print('\nCASE #' + str(casesdone) + ' N is: ' + str(N))

    #####################
    # Start Solution Here
    #####################

    # Insomnia can ONLY happen if the number is 0   
    if N == 0:
        answer = 'INSOMNIA'
    else:
        multiplier = 1
        digitPresent = 0
        while True:
            digitPresent = digitPresent | checkDigits(multiplier*N)
            if SHOW_DEBUG:
                print('Counting ' + str(multiplier*N) + ' ...zzzzz')
            if digitPresent == (2**10) - 1:
                break
            multiplier += 1
        answer = str(multiplier*N)

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
