"""

@author: Nishant Kumar
Date: 10-04-2016

"""

__author__ = 'Nishant Kumar'

import os

def get_count(pattern):
    count = 0
    status = pattern[0]

    for index in range(1, len(pattern)):
        if pattern[index] != pattern[index - 1]:
            count += 1
            status = '-' if pattern[index - 1] == '+' else '+'

    if status == '-':
        count += 1

    return count

def main():
    home_dir = r'C:\Users\Nishant\Dropbox\CodeBase\Coding Competitions\GoogleCodeJam_2016\Qualification Round'

    input_file  = os.path.join(home_dir, 'B-large.in')
    output_file = os.path.join(home_dir, 'B-large.out')

    f = open(input_file, 'r')
    o = open(output_file, 'w')

    total_cases = int(f.readline())
    lst = list(f)

    case_no = 1

    while case_no <= total_cases:
        pattern = lst[case_no-1].strip()
        o.write ("Case #%s: %s\n" %(case_no, get_count(pattern)))
        case_no += 1

    f.close()
    o.close()

if __name__ == '__main__':
    main()