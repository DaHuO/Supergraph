import os
import sys
import itertools

def output_format(answer,test_case):
    output = "Case #%d:" % (test_case+1)
    output += " %s" % str(answer)
    #output +="\n"
    return output



if __name__ == "__main__":
    #f = open("A-practice.in",'r')
    f = open("A-large.in",'r')
    #f = open("A-small-attempt0.in",'r')
    test_cases = int(f.readline())
    #out = open("results_A_p_0.txt",'w')
    #out = open("results_A_s_0.txt",'w')
    out = open("results_A_l_0.txt",'w')
    

    print test_cases
    for i in range(test_cases):
        print "\nTest case #%d"%i
        word = f.readline()
        l_w = word[0]
        for s in list(word[1:]):
            if s > l_w[-1]:
                if s < l_w[0]:
                    l_w = l_w + s
                else:
                    l_w = s+ l_w
            else:
                if s < l_w[0]:
                    l_w = l_w + s
                else:
                    l_w = s + l_w
            #print l_w

        answer = l_w
        output = output_format(answer,i)
        out.write(output)
