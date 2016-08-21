#!/usr/bin/env python3

in_file = open('D-small-attempt0.in.txt', 'r')

for case in range(1, int(in_file.readline().strip()) + 1):
    input_data = [int(x) for x in in_file.readline().strip().split(' ')]
    print('Case #{}: {}'.format(case, ' '.join([str(x) for x in range(1, input_data[2] + 1)])))
