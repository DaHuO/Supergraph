import sys
import copy
import math
from collections import deque

#obtain the name of the input
def fileName():
    filename = 'input'
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        print("File was not indicated")
        exit()
    return filename

fn = fileName()
file = open(fn, 'r')
out = open('output', 'w')

line_number = 1;
testcase = 1
max_testcases = 0
tc_ln = 0

digits = [0] * 10
print(digits)

while True:
    line = file.readline()
    if line:
        line = line.replace("\n","")
        inputs = line.split(" ")
        #how many test cases are
        if line_number == 1:
            max_testcases = int(inputs[0])
            line_number = 2
            tc_ln = 0
            continue
        
        N = int(inputs[0])
        ans = "INSOMNIA"
        if N > 0:
            for x in range(10):
                digits[x] = 0

            N_i = 0
            while(True):
                N_i = N_i + N
                s_N_i = str(N_i)
                for j in range(len(s_N_i)):
                    act_dig = int(s_N_i[j])
                    digits[act_dig] = digits[act_dig] + 1

                get_out = True
                for x in range(10):
                    if digits[x] == 0:
                        get_out = False
                        break
                if get_out:
                    break
            ans = str(N_i)

        out.write("Case #"+str(testcase)+": "+ans+"\n")
        tc_ln = 0
        testcase = testcase + 1
        line_number += 1
    else:
        break
file.close()
out.close()
exit()