import sys
import fileinput

def answer(inpt):
    lst = inpt.split(' ')
    lst = [int(i) for i in lst]
    k, c, s = lst
    rst = ""
    if c==1 or k==1:
        if s < k:
            return "IMPOSSIBLE"
        else:
            for indx in range(1, k+1):
                rst += (str(indx) + " ")
            return rst.strip()
    else:
        if s < k-1:
            return "IMPOSSIBLE"
        else:
            for indx in range(2, k+1):
                 rst += (str(indx) + " ")
            return rst.strip()
    
    

inputs  = [line.rstrip() for line in fileinput.input()]
for idx in range(1, int(inputs[0])+1):
    print "Case #" + str(idx) + ": " +  str(answer(inputs[idx]))
