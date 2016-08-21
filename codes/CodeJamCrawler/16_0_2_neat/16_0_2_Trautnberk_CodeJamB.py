#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mhlozanka
#
# Created:     09/04/2016
# Copyright:   (c) mhlozanka 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
input = r'd:\A-small-practice.in'
input2  = r'd:\A-small-practice - Copy.in'
output = r'd:\out.txt'

def check(pancakes):
    return not(False in pancakes);

def flip(pancakes, pos):
    tmp = pancakes[0:pos+1];
    tmp = tmp[::-1];
    for i in range(pos+1):
        pancakes[i] = not tmp[i];
    return pancakes;


def solve(pancakes):
    flips = 0;
    stack =[]
    for i in range(len(pancakes)):
        if pancakes[i] =='+':
            stack.append(True);
        else:stack.append(False);

    while not check(stack):
        if stack[0]:
            i=0;
            while stack[i+1] and i<len(stack):
                i+=1;
            stack = flip(stack,i);

        else:
            pos = (len(stack) - 1) - stack[::-1].index(False);
            stack = flip(stack, pos);

        flips += 1;
    return flips;


def main():
    out = open(output,'w');
    with open(input,'r') as f:
        cases = int(f.readline());
        caseNum = 1;
        for case in range(cases):
            pancakes = f.readline().strip();
            res = solve(pancakes);

            msg = 'Case #{0}: {1}\n'.format(caseNum,res)
            out.write(msg);
            caseNum+=1;
    out.close()


if __name__ == '__main__':
    main()