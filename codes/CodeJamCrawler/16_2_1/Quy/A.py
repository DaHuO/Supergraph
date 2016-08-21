__author__ = "Quy Doan"

import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file,"r") as reader:
    with open(output_file, "w") as writer:
        '''Do stuffs'''
        c_number = ["ZERO", "WTO", "XSI", "URFO", "FIVE", "RTHEE", "TEIGH", "INNE", "ONE", "SEVEN"]
        a_number = ['0','2','6','4','5','3','8','9','1','7']
        num_of_tests = int(reader.readline())
        for test in range(num_of_tests):
            s = reader.readline()
            fr = [0 for x in range(100)]
            for c in s:
                fr[ord(c)] += 1
            
            res = ''
            for idx  in range(10):
                cn = c_number[idx]
                while fr[ord(cn[0])] > 0:
                    res += a_number[idx]
                    for c in cn:
                        fr[ord(c)] -= 1

            writer.write("Case #"+str(test+1)+": "+ ''.join(sorted(res))+'\n')


            
