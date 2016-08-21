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
import math;

input = r'd:\A-small-practice.in'
input2  = r'd:\A-small-practice - Copy.in'
output = r'd:\out.txt'


def isPrime(n):
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def checkBases(number):
    for base in range(2,11):
        if isPrime(int(number,base)):
            return False;
    return True;

def findDivisor(number):
    if number % 2 == 0:
        #return number/2;
        return 2;
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            #return number/i;
            return i;

def generate(length, count):
    end = int((int(length)-2)*'1',2);
    out = "";
    counter = 0;
    for i in range(end+1):
        diff = int(length)-2 - len(bin(i)[2:]) ;
        if diff<0:
            diff = 0;
        number = '1'+diff*'0'+ bin(i)[2:]+'1';

        if not checkBases(number):
            continue;

        out = out + number;

        for base in range(2,11):
            out = out + " " + str(findDivisor(int(number,base)));
        out = out + "\n";
        counter += 1;
        if counter == int(count):
            return out;



def main():
    out = open(output,'w');
    with open(input2,'r') as f:
        cases = int(f.readline());
        caseNum = 1;
        for case in range(cases):
            length,numbers = f.readline().strip().split();

            res = generate(length,numbers);

            msg = 'Case #{0}:\n{1}\n'.format(caseNum,res)
            out.write(msg);
            caseNum+=1;
    out.close()


if __name__ == '__main__':
    main()

