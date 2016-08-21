"""

@author: Nishant Kumar
Date: 08-05-2016

"""

__author__ = 'Nishant Kumar'

from collections import defaultdict
import os
import string

def plan(N, P):
    my_plan = []
    parties = [c for c in string.ascii_uppercase]
    #print(parties)
    total = sum(P)
    #print(total)
    while total > 0:
        max_value = max(P)
        #print(max_value, type(P[0]))
        max_index = [i for i in range(0, N) if P[i] == max_value]
        #print("max_value=%s" %(max_value))
        #print("max_index=%s" %(max_index))

        if total == 2 or len(max_index) == 2:
            my_plan.append(parties[max_index[0]] + parties[max_index[1]])
            P[max_index[0]] -= 1
            P[max_index[1]] -= 1
            total -= 2
            continue

        if len(max_index) == 1:
            my_plan.append(parties[max_index[0]])
            P[max_index[0]] -= 1
            total -= 1
            continue

        if len(max_index) > 2:
            my_plan.append(parties[max_index[0]])
            P[max_index[0]] -= 1
            total -= 1

    return my_plan


def main():
    home_dir = r'C:\Users\Nishant\Dropbox\CodeBase\Coding Competitions\GoogleCodeJam_2016\Round_1C'

    input_file  = os.path.join(home_dir, 'A-large.in')
    output_file = os.path.join(home_dir, 'A-large.out')

    f = open(input_file, 'r')
    o = open(output_file, 'w')

    total_cases = int(f.readline())
    inputs = list(f)
    case_no = 1
    index = 0

    while case_no <= total_cases:
        N = int(inputs[index].strip())
        P = inputs[index+1].strip().split()
        P = [int(p) for p in P]

        index += 2

        my_plan = plan(N, P)
        o.write ("Case #%s: %s\n" %(case_no, ' '.join(my_plan)))
        case_no += 1

    f.close()
    o.close()

if __name__ == '__main__':
    main()