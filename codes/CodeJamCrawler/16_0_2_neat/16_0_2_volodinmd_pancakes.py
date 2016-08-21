from __future__ import print_function
__author__ = 'volodin'


def flip(line):
    return (line.replace('+', '%temp%').replace('-', '+').replace('%temp%', '-'))[::-1]


def pick_last_symbol(line):
    if line[0] == '-':
        return len(line)
    #get index of first minus in line
    return line.index('-')


def solve(line):
    N = 0
    while True:
        line = line.rstrip('+')
        if not line:
            return N
        n = pick_last_symbol(line)
        line = flip(line[0:n]) + line[n:]
        N += 1


input = open('pancakes-big.in', 'r')
output = open('pancakes-big-out.txt', 'w')
T = input.readline()
for i in range(0, int(T)):
    answer = solve(input.readline().rstrip('\r\n'))
    answer = "Case #{0}: {1}\n".format(i + 1, answer)
    print(answer, end='')
    output.write(answer)
