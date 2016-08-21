import math

Input = open('./input.in','r')
Output = open('./output.out','w+')
index = 1
N = -1
for eachline in Input:
    if N==-1:
        N = int(eachline)
    else:
        T = int(eachline)
        if T !=0:
            all_digi = [0]*10
            for i in range(1,1000000):
                digi = [(i*T)/(10**n)-(i*T)/(10**(n+1))*10 for n in range(int(math.log(i*T)/math.log(10))+1)]
                all_digi = [all_digi[n]+1 if n in digi else all_digi[n] for n in range(10)]
                if 0 not in all_digi:
                    print >> Output, "case #%d: %d" % (index,i*T)
                    break
        else:
            print >> Output, "case #%d: INSOMNIA" % (index)
        if index==N:
            break
        index += 1
        
Output.close()
Input.close()
