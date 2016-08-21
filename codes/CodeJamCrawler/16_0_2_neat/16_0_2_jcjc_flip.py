import sys

f = open(sys.argv[1])
T = int(f.readline())
S = f.readlines()

for t in range(T):
    s = S[t][:-1]
    num = 0
    current = s[0]
    for pancake in s[1:]:
        if current != pancake:
            num = num + 1
            current = pancake
    if current == '-':
        num = num + 1
    print 'Case #{}: {}'.format(t+1, num)


