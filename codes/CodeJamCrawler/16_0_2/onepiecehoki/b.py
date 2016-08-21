import re

def reduce(s):
    s = re.sub(r'(.)\1+', r'\1', s)
    return s

T = int(raw_input())

for t in xrange(1,T+1):
    S = raw_input()
    S_reduced = reduce(S)
    result = len(S_reduced)
    if len(S_reduced) > 0 and S_reduced[-1] == '+':
        result -= 1
    print('Case #%d: %d' %(t, result))





