import itertools

def compute(orig, curr, K):
    st = list(curr)
    for i in xrange(len(st)):
        if st[i] == 'G':
            st[i] = K * 'G'
        else:
            st[i] = orig
    return ''.join(st)

def contains_g(s):
    for x in xrange(len(s)):
        if s[x] == 'G':
            return True
    return False 

T = int(raw_input())
for t in xrange(T):
    inp = map(int, raw_input().split(' '))
    K = inp[0]; C = inp[1]; S = inp[2];
    perms = []
    temp_set = set([])
    for x in xrange(K):
        perms.append('G')
        perms.append('L')
    for i in itertools.permutations(perms, K):
        temp_set.add(i)
    perms = list(temp_set)
    
    sequences = []
    
    for perm in perms:
        st = ''.join(perm)
        new_st = st
        for x in xrange(C-1):
            new_st = compute(st, new_st, K)
        sequences.append(new_st)
    
    l = []
    for i in itertools.combinations([x for x in xrange(len(sequences[0]))], S):
        l.append(i)
    
    # if both elms are L and contains_g() is False => eliminate
    want = []
    for item in l:
        flag2 = 0
        for sequence in sequences:
            flag = 0
            for elm in item:
                if sequence[elm] == 'G':
                    flag = 1 # We don't want this
            if flag != 1:
                if not contains_g(sequence):
                    flag2 = 1 # We want this
                else:
                    flag2 = 0
                    print "i reach"
                    break
        if flag2 == 1:
            want.append(item)
    print l
    print want
