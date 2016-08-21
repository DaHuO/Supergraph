def rm(S, word):
    for c in word:
        S.remove(c)
    return S

T = input()
for t in range(T):
    S = list(raw_input().strip())
    nums = []

    while S.count('Z'):
        S = rm(S, 'ZERO')
        nums.append(0)
    while S.count('X'):
        S = rm(S, 'SIX')
        nums.append(6)
    while S.count('S'):
        S = rm(S, 'SEVEN')
        nums.append(7)
    while S.count('W'):
        S = rm(S, 'TWO')
        nums.append(2)
    while S.count('V'):
        S = rm(S, 'FIVE')
        nums.append(5)
    while S.count('F'):
        S = rm(S, 'FOUR')
        nums.append(4)
    while S.count('R'):
        S = rm(S, 'THREE')
        nums.append(3)
    while S.count('T'):
        S = rm(S, 'EIGHT')
        nums.append(8)
    while S.count('O'):
        S = rm(S, 'ONE')
        nums.append(1)
    while S.count('N'):
        S = rm(S, 'NINE')
        nums.append(9)
    
    s = ''.join(map(str, sorted(nums)))

    print 'Case #%d: %s'%(t+1, s)
