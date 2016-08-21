########################################################
#  - Google Code Jam 2016 Round 1a
# Problem B
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

    inputrows = []
    for i in range(2*N-1):
        inputrows.append(list(map(int,input().split(' '))))

    # Echo the inputs for debugging
    if SHOW_DEBUG:
        print('\nCASE #' + str(casesdone) + ' N: ' + str(N) +
              '\nInputrows: ' + str(inputrows))

    #####################
    # Start Solution Here
    #####################

    numbercount = {}
    for row in inputrows:
        for number in row:
            try:
                numbercount[number] += 1
            except:
                numbercount[number] = 1

    solution = []
    for key in numbercount.keys():
        if numbercount[key]%2 != 0:
            solution.append(key)

    solution.sort()

    solutionstr = ''
    for char in solution:
        solutionstr += str(char)
        solutionstr += ' '

    solutionstr.strip()

    if SHOW_DEBUG:
        print('numbercount: ' + str(numbercount))

    #############################
    # Solve and print the answer!
    #############################
    print('Case #' + str(casesdone) + ': ' + solutionstr)





    #############################
    # Some code to print out the script's performance, if that option is enabled
    if SHOW_PERF_TIMES and casesdone % 10 == 0:
        stop = time.clock()
        print('TIME:  Cases ' + str(casesdone-10) + ' to ' + str(casesdone) + ' TOTAL: ' + str(stop-start) + ' AVG: ' + str((stop-start)/10))
        start = time.clock()

veryend = time.clock()
if SHOW_PERF_TIMES:
    print('\nTIME:  Total Program Time: ' + str(veryend-verystart))
