from itertools import combinations
T = int(input())
N, J = list(map(int, input().split()))

odd = (1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31)
even = (2,4,6,8,10,12,14,16,18,20,22,24,26,28,30)

pairs = []

for o1, o2 in combinations(odd, 2):
    for e1, e2 in combinations(even, 2):
        pairs.append((o1,o2,e1,e2))
    if len(pairs) > 500:
        break

pairs = pairs[:500]

for t in range(1, T + 1):
    print('Case #{0}:'.format(t))
    for o1, o2, e1, e2 in pairs:
        num = '{0:b}'.format(2**31 + 1 + 2**o1 + 2**o2 + 2**e1 + 2**e2)
        print(num, end=' ')
        for i in range(2, 10):
            base_rep = int(num, i)
            assert(base_rep % (i + 1) == 0)
            print(i + 1, end=' ')
        assert(int(num, 10) % 11 == 0)
        print(11)
