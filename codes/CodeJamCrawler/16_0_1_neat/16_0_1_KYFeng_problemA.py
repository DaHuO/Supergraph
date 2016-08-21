f = open('A-large.in', 'r')
fo = open('a-large-out', 'w')
T = int(f.readline())
for caseID in range(1, T+1):
    print(caseID)
    N = int(f.readline())
    if N == 0:
        fo.write('Case #{}: INSOMNIA\n'.format(caseID))
        continue
    digits = set([])
    cnt = 0
    number = N
    while len(digits) < 10:
        for c in str(number):
            digits.add(c)
        number += N
        cnt += 1 
    fo.write('Case #{}: {}\n'.format(caseID, number-N))