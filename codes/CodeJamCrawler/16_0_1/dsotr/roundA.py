import os, sys

def solve_case(input):
    print(input)
    if input == '0':
        return 'INSOMNIA'
    increment = int(input)
    N = increment
    s=set(tuple(input))
    while len(s) < 10:
        #print(s)
        N += increment
        for e in str(N):
            s.add(e)
    return N

if __name__=='__main__':
    #path = './A-small-attempt0.in'
    path = './A-large.in'
    out = open('./out.txt','w',  newline='')
    count = 1
    with open(path) as f:
        f.readline()
        for case in f:
            out.write("Case #%i: %s\n" %(count, solve_case(case.strip())))
            count += 1
    out.close()
    print('done')