import sys
#import Counting_Sheep


fh = open('prob1.txt','w')
readHead = False
testcase_num = int(input())
testcase_idx = 0
while testcase_idx < testcase_num:
    tgt_digit = [str(i) for i in range(0,10)]
    N = int(input())
    fh.write("Case #"+str(testcase_idx+1)+':')
    testcase_idx += 1
    for T in range(1,101):
        nT = list(str(T*N))
        for dig in nT:
            if dig in tgt_digit:
                tgt_digit.remove(dig)
        if len(tgt_digit) == 0:
            fh.write(' '+''.join(nT)+'\n')
            break
    else:
        fh.write(' INSOMNIA\n')

fh.close()
