#!/usr/bin/env python
import sys

def main():
    if len(sys.argv) < 3:
        print('a.py <limit> <input>')

    limit = int(sys.argv[1])
    with open(sys.argv[2], 'r') as input_file:
        num_cases = int(input_file.readline())
        case = 1
        while num_cases > 0:
            line = int(input_file.readline())
            iters = count_sheep(limit, line)
            print('Case #{}: {}'.format(str(case), str(iters)))
            case += 1
            num_cases -= 1


def count_sheep(limit, line):
    values = set([0,1,2,3,4,5,6,7,8,9])
    current = set()
    for i in range(limit):
        idx = i + 1
        calc = str(idx*line)
        current.update([int(x) for x in calc])
        if (sorted(current) == sorted(values)):
            return line * idx
    return 'INSOMNIA'
    #for i in range(1000000):
        


if __name__ == "__main__":
    main()
