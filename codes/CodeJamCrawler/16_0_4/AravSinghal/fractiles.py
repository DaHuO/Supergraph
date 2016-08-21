from redef_io import *

t = int(input())

for it in range(t):
    line = input().split(' ')

    k = int(line[0])
    c = int(line[1])
    s = int(line[2])

    # Evil laugh
    print_file(' '.join([str(x) for x in range(1, s + 1)]))
