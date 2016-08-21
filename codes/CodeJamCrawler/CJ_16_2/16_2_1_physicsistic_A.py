import sys

T = {0: 'ZERO', 
    1: 'ONE', 
    2: 'TWO',
    3: 'THREE',
    4: 'FOUR',
    5: 'FIVE',
    6: 'SIX',
    7: 'SEVEN',
    8: 'EIGHT', 
    9: 'NINE'}

P = dict()

for k,v in T.iteritems():
    d = dict()

    for c in v:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    P[k] = d

print P

def solve(S):
    A = dict()
    for c in S:
        if c in A:
            A[c] += 1
        else:
            A[c] = 1
    print A

    answer = []

    ## 0
    if 'Z' in A:
        n = A['Z']
        for k, v in P[0].iteritems():
            A[k] -= n * v
            if A[k] == 0:
                A.pop(k, None)
        answer.extend([0]*n)

    ## 2
    if 'W' in A:
        n = A['W']
        for k, v in P[2].iteritems():
            A[k] -= n * v
            if A[k] == 0:
                A.pop(k, None)
        answer.extend([2]*n)

    ## 4
    if 'U' in A:
        n = A['U']
        for k, v in P[4].iteritems():
            A[k] -= n * v
            if A[k] == 0:
                A.pop(k, None)
        answer.extend([4]*n)

    ## 6
    if 'X' in A:
        n = A['X']
        for k, v in P[6].iteritems():
            A[k] -= n * v
            if A[k] == 0:
                A.pop(k, None)
        answer.extend([6]*n)

    ## 8
    if 'G' in A:
        n = A['G']
        for k, v in P[8].iteritems():
            A[k] -= n * v
            if A[k] == 0:
                A.pop(k, None)
        answer.extend([8]*n)

    ## 3
    if 'R' in A:
        n = A['R']
        for k, v in P[3].iteritems():
            A[k] -= n * v
            if A[k] == 0:
                A.pop(k, None)
        answer.extend([3]*n)

    ## 5
    if 'F' in A:
        n = A['F']
        for k, v in P[5].iteritems():
            A[k] -= n * v
            if A[k] == 0:
                A.pop(k, None)
        answer.extend([5]*n)

    ## 7
    if 'S' in A:
        n = A['S']
        for k, v in P[7].iteritems():
            A[k] -= n * v
            if A[k] == 0:
                A.pop(k, None)
        answer.extend([7]*n)

    ## 1
    if 'O' in A:
        n = A['O']
        for k, v in P[1].iteritems():
            A[k] -= n * v
            if A[k] == 0:
                A.pop(k, None)
        answer.extend([1]*n)

    ## 9
    if 'I' in A:
        n = A['I']
        for k, v in P[9].iteritems():
            A[k] -= n * v
            if A[k] == 0:
                A.pop(k, None)
        answer.extend([9]*n)
    answer.sort()
    ''.join(map(str, answer))
    return ''.join(map(str, answer))

def io(filename):
    output = open(filename.split('.')[0]+'.out', 'w')
    with open(filename, 'r') as f:
        T = int(f.readline())
        for t in range(T):
            S = f.readline().rstrip('\n')
            string = "Case #{n}: {y}".format(n=t+1, y=solve(S))
            print string
            print "======================================================="
            output.writelines(string+'\n')   
 
if __name__ == '__main__':
    input_file = sys.argv[1]
    io(input_file)