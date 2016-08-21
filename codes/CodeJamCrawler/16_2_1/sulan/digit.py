import math
import sys
import collections

def print_result (case_num,result):
    print('Case #{}: {}'.format(case_num,result))

T = int(input())
for case_num in range(1,T+1):
    ss = input()
    letters = collections.Counter(ss)
    dd = [0,8,3,2,6,4,7,1,5,9]
    words = ['ZERO','EIGHT','THREE','TWO','SIX','FOUR','SEVEN','ONE','FIVE','NINE']
    r = []
    for i,L in enumerate('ZGHWXUSOVI'):
        try:
            count = letters[L]
        except KeyError:
            continue
        word = words[i]
        if count > 0:
            r += [dd[i]]*count
            for l in word:
                assert letters[l] >= count, 'Not enough letters'+str(i)+str(l)
                letters[l] -= count
    assert len(list(letters.elements())) == 0, 'There were some remaining letters'
    r.sort()
    print_result(case_num,''.join(map(str,r)))



