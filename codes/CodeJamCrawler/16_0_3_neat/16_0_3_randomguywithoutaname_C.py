## Problem C

raw_input()
N, J = tuple(int(n) for n in raw_input().split(' '))
assert N % 2 == 0

divisibilities = [3, 2, 5, 2, 7, 2, 3, 2, 11]
divstr = ' '.join(str(s) for s in divisibilities)

def check(s):
    for i in range(2, 11):
        assert int(s, i) % divisibilities[i-2] == 0

print 'Case #1:'

for i in range(0, J):
    numstr = ['1'] * N
    fillstr = format(i, '0%db' % (N/2 - 1))
    for j in range(0, len(fillstr)):
        numstr[2*j+1] = fillstr[j]
        numstr[2*j+2] = fillstr[j]
    num = ''.join(numstr)
    check(num)
    print '%s %s' % (num, divstr)