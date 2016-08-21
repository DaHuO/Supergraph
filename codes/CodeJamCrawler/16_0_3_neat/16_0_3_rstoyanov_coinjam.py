#!/usr/bin/python
def base_calc():
    global Bases,num
    #Base calculator
    for j in xrange(2,11):
        base = j - 2
        Bases[base] = int(num,j)

def genN():
    global N,num,k
    old_num = num
    while num[0] != '1' or num[len(num)-1] != '1' or len(num) != N or old_num==num:
        k = int(num,2)
        k += 1
        num = "{0:b}".format(k)

T = int(raw_input())
for t in xrange(T):
    inp = raw_input()
    N = int(inp.split(' ')[0])
    J = int(inp.split(' ')[1])
    num = '1' + '0' * (N-2) + '1'
    print 'Case #' + str(t+1) + ':'
    while J != 0:
        Bases = [0] * 9
        Divs = [0] * 9
        fl = 0
        i = -1
        base_calc()
        for k in Bases:
            i += 1
            for m in xrange(2,1000):
                if k % m == 0 and m != int(num,2):
                    Divs[i] = m
                    break
            if Divs[i] == 0:
                fl=1
                break
        if fl == 0:
            J -= 1
            output = num
            for i in Divs:
                output += ' ' + str(i)

            print output
            # print Bases,int(num,2)
        genN()
