import os, sys
flip = {'-':'+', '+':'-'}
def solve_case(input, i):
    if not '-' in input:
        return i
    first = input[0]
    count = 1
    for e in input[1:]:
        if e == input[0]:
            count += 1
        else:
            break
    top = flip[first] * count
    return solve_case(top + input[len(top):], i+1)

if __name__=='__main__':
    #path = './B-small-attempt0.in'
    path = './B-large.in'
    out = open('./out.txt','w',  newline='')
    count = 1
    with open(path) as f:
        f.readline()
        for case in f:
            out.write("Case #%i: %i\n" %(count, solve_case(case.strip(), 0)))
            count += 1
    out.close()
    print('done')