'''
@author Tristan Bodding-Long
@email tbodding@gmail.com

Bleatrix Trotter the sheep has devised a strategy that helps her fall asleep faster. First, she picks a number N. Then she starts naming N, 2 × N, 3 × N, and so on. Whenever she names a number, she thinks about all of the digits in that number. She keeps track of which digits (0, 1, 2, 3, 4, 5, 6, 7, 8, and 9) she has seen at least once so far as part of any number she has named. Once she has seen each of the ten digits at least once, she will fall asleep.

Bleatrix must start with N and must always name (i + 1) × N directly after i × N. For example, suppose that Bleatrix picks N = 1692. She would count as follows:

N = 1692. Now she has seen the digits 1, 2, 6, and 9.
2N = 3384. Now she has seen the digits 1, 2, 3, 4, 6, 8, and 9.
3N = 5076. Now she has seen all ten digits, and falls asleep.
What is the last number that she will name before falling asleep? If she will count forever, print INSOMNIA instead.

Input

The first line of the input gives the number of test cases, T. T test cases follow. Each consists of one line with a single integer N, the number Bleatrix has chosen.

Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the last number that Bleatrix will name before falling asleep, according to the rules described in the statement.'''

from codecs import open as cOpen
from sys import argv


def readInput(path):
    ''' Will fail on bad input, TypeError
        Trust the input to not contain floats
    '''
    with cOpen(path, encoding='utf-8') as inFile:
        # of test cases
        inFile.readline()
        for line in inFile:
            yield int(line.strip())
        
def main():
    caseNo = 0
    for seed in readInput(argv[1]):
        caseNo += 1
        if seed == 0:
            print(u'Case #{}: INSOMNIA'.format(caseNo))
        else:
            unseen = set([str(e) for e in range(10)])
            multiplier = 1
            while True:
                num = seed*multiplier
                seen = set([str(e) for e in str(num)])
                unseen = unseen - seen
                if len(unseen) == 0:
                    break
                multiplier += 1
            print(u'Case #{}: '.format(caseNo) + str(num))
                    
            


if __name__ == '__main__':
    main()