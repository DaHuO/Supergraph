import sys

def flip(n):
    t = ''
    for i in n:
        if i is '+':
            t = '-' + t
        else:
            t = '+' + t
    return t


def solve(n):
    #removes the /n
    n = n[:-1]
    processed = {}

    def recur(n, objective):
        if not n:
            return 0

        processed[n] = 1
        last = n[-1]

        flipped = flip(n)

        if last is not objective:
            move = 1
        else:
            move = 0
            
        if flipped not in processed:

            return min(1 + recur(flipped, objective), move + recur(n[:-1], last))
        else:
            return move + recur(n[:-1], last)

    return recur(n, '+')


input = sys.argv[1]

with open(input, 'r') as f:
    input = f.readlines()

f2 = open('out.txt', 'w')

t = int(input[0])
for i in xrange(1, t + 1):
    n = input[i]
    f2.write( "Case #{}: {}".format(i, solve(n))+'\n')


