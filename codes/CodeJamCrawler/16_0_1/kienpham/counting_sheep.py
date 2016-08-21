#!/usr/bin/env python3
import sys


def print_output(case_number, answer='INSOMNIA'):
    print("Case #{}: {}".format(case_number, answer))


def count_me(cases, data):
    all_numbers = {i: i for i in range(0, 10)}
    cache = {}

    for i in range(0, cases):
        if data[i] == 0:
            print_output(i+1)
        else:
            j = 1
            while True:
                tmp = j * data[i]
                for x in str(tmp):
                    if x not in cache:
                        cache[int(x)] = int(x)
                # print(cache)
                # exit()
                j += 1
                if len(cache) == len(all_numbers):
                    print_output(i+1, tmp)
                    cache = {}
                    break


if __name__ == "__main__":
    test_cases = ''

    # {0:0, 1:1,...9:9}


    if(len(sys.argv)) == 1:
        input_file = sys.argv[0].replace('./', '').replace('.py', '.in')
    else:
        input_file = sys.argv[1]

    with open(input_file) as f:
        data = []
        for N in f:

            if not test_cases:
                test_cases = int(N)
            else:
                data.append(int(N))
        count_me(test_cases, data)

            # print(line)

    # print(test_cases)
    # print_output(1)

# 10 000 000
