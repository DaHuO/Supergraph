"""

@author: Nishant Kumar
Date: 10-04-2016

"""

__author__ = 'Nishant Kumar'

import os

def main():
    home_dir = r'C:\Users\Nishant\Dropbox\CodeBase\Coding Competitions\GoogleCodeJam_2016\Qualification Round'

    input_file  = os.path.join(home_dir, 'A-large.in')
    output_file = os.path.join(home_dir, 'A-large.out')

    precomputed_result = []
    precomputed_result.append('INSOMNIA')

    for i in range(1, 1000001):
        found = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        num = 1
        while (True):
            mul = str(num * i)
            for digit in mul:
                found[int(digit)] = digit

            if -1 not in found:
                precomputed_result.append(mul)
                break
            if num > 200:
                precomputed_result.append('INSOMNIA')
                break
            num += 1

    f = open(input_file, 'r')
    o = open(output_file, 'w')

    total_cases = int(f.readline())
    lst = list(f)

    case_no = 1

    while case_no <= total_cases:
        number = int(lst[case_no-1])
        o.write ("Case #%s: %s\n" %(case_no, precomputed_result[number]))

        case_no += 1

    f.close()
    o.close()

if __name__ == '__main__':
    main()