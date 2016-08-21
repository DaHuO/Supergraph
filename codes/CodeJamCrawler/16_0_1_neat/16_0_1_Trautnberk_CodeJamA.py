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


def check(numbers):
    res = True;
    for num in range(10):
        res = res & (num in numbers);
    return res;

def count(start):
    if int(start) == 0:
        return 'INSOMNIA'

    numbers = []
    currentNum = start;
    i=1
    n = 10000;
    while i<=n:
        for ch in currentNum:
            if  int(ch) not in numbers:
                numbers.append(int(ch));
        if check(numbers):
            return currentNum;
        i+=1;
        currentNum = str(i*int(start));
    return 'INSOMNIA'


def main():
    out = open(output,'w');
    with open(input,'r') as f:
        cases = int(f.readline());
        caseNum = 1;
        for case in range(cases):
            num = f.readline().strip();
            res = count(num);

            msg = 'Case #{0}: {1}\n'.format(caseNum,res)
            out.write(msg);
            caseNum+=1;
    out.close()


if __name__ == '__main__':
    main()