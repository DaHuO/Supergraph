def compete(lineup):
    ret = []
    for i in xrange(len(lineup)/2):
        first = lineup[2*i]
        second = lineup[2*i+1]
        if first == second: return None
        if first == 'R':
            if second == 'P': ret.append('P')
            else: ret.append('R')
        elif first == 'P':
            if second == 'S': ret.append('S')
            else: ret.append('P')
        else:
            if second == 'R': ret.append('R')
            else: ret.append('S')
    return ret

import itertools

IN = open('input.txt', 'r')
OUT = open('output.txt', 'w')

NUM_TESTS = int(IN.readline())

for test in xrange(NUM_TESTS):
    N, R, P, S = map(int,IN.readline().split())
    
    x = ('P' * P) + ('R' * R) + ('S' * S)
    answer = 'IMPOSSIBLE'
    
    for lineup in itertools.permutations(x):
        temp = lineup
        while lineup and len(lineup) > 1:
            lineup = compete(lineup)
        if lineup:
            answer = ''.join(temp)
            break
    
    OUT.write('Case #{}: {}\n'.format(test+1, answer))
    print test+1, answer

IN.close()
OUT.close()
