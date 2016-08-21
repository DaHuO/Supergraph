import sys
def solve(n):
    seen = {}
    digits = {}

    mul = 1
    next = mul*n

    while(next not in seen.keys()):
        for i in str(next):
            digits[i] = 1
        print digits
        print next
        if len(digits.keys()) is 10:
            return next

        seen[next]=1
        mul+=1
        next = mul*n

    return "INSOMNIA"


input = sys.argv[1]

with open(input, 'r') as f:
    input = f.readlines()

f2 = open('out.txt', 'w')

t = int(input[0])
for i in xrange(1, t + 1):
    n = int(input[i])
    f2.write( "Case #{}: {}".format(i, solve(n))+'\n')


