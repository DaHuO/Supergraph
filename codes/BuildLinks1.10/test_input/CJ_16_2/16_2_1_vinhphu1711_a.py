import itertools

T = int(raw_input())

arr = ['ZERO','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE']

mapping = {}
for i in range(10):
    for c in arr[i]:
        mapping.setdefault(c, [])
        mapping[c].append(i)

#print mapping
def check(w, s):
    for i in w:
        if i not in s:
            return False
    return True

def mystrip(w, s):
    for i in w:
        s = s.replace(i, '', 1)
    return s

def findsubsets(S, m):
    return set(itertools.product(S, repeat=m))

def check_final(digits, s):
    ss = ''
    for d in digits:
        ss += arr[int(d)]
    return len(ss) == len(s) and sorted(ss) == sorted(s)

for t in range(T):
    S0 = raw_input()
    #start_index = 0

    #while start_index <= 9:
    S = S0[:]

    possible_digits = set([])
    for c in S:
        possible_digits.update(mapping[c])

    #print possible_digits
    res = ''
    #print range(len(S)/5, len(S)/3+1)
    for n in range(len(S)/5, len(S)/3+1):
        possible_combs = findsubsets(possible_digits, n)
        for possible_comb in possible_combs:
            SS = ''
            for digit in possible_comb:
                SS += arr[digit]
            #print SS
            if len(SS) == len(S0) and sorted(SS) == sorted(S0):
                res = ''.join([str(i) for i in sorted(possible_comb)])
                found = True
                break
                #while len(S) > 0 and check(wor,)
        if res:
            break

    #if not check_final(res, S0):
    #    print 'MOTHER'
    #    exit()
    print 'Case #%d: %s' % (t+1, res)