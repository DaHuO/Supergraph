import os
import sys
import itertools
import numpy as np
def output_format(answer,test_case):
    output = "Case #%d:" % (test_case+1)
    output += " %s" % " ".join([str(x) for x in answer])
    output +="\n"
    return output



if __name__ == "__main__":
    #f = open("B-practice.in",'r')
    f = open("B-large.in",'r')
    #f = open("B-small-attempt0.in",'r')
    test_cases = int(f.readline())
    #out = open("results_B_p_0.txt",'w')
    #out = open("results_B_s_0.txt",'w')
    out = open("results_B_l_0.txt",'w')
    

    print test_cases
    for i in range(test_cases):
        n = int(f.readline())
        print n
        list_matrix = [[] for v in range(2*n -1)]
        count_heights = {}
        for j in range(2*n-1):
            list_matrix[j] = [int(x) for x in list(f.readline().strip("\n").split(" "))]
            for el in list_matrix[j]:
                count_heights[el] = count_heights.get(el,0) + 1
        found = []
        for key in count_heights.keys():
            if count_heights[key] %2 ==1:
                found.append(key)



        print "\nTest case #%d"%i
        answer = sorted(found)
        output = output_format(answer,i)
        out.write(output)
