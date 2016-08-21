import os, sys

def solve_case(input):
    k,c,s = map(lambda x: int(x), input.split(' '))
    print(k,c,s)
    result=[]
    if s >= k:
        for i in range(k):
            result.append(i+1)
        return ' '.join(map(str,result))
    if s == 1:
        return 'IMPOSSIBLE'

if __name__=='__main__':
    path = './D-small-attempt0.in'
    #path = './A-large.in'
    out = open('./out.txt','w',  newline='')
    count = 1
    with open(path) as f:
        f.readline()
        for case in f:
            out.write("Case #%i: %s\n" %(count, solve_case(case.strip())))
            count += 1
    out.close()
    print('done')