filename = 'A-large-attempt0.out'
target = open(filename, 'w')

t = int(input())
myset = set()

for i in range(t):
    k = int(input())
    base = k
    if k == 0:
        target.write('Case #%d: INSOMNIA\n' % (i + 1))
    else:
        while True:
            for char in str(k):
                myset.add(char)
            if len(myset) == 10:
                target.write('Case #%d: %d\n' % (i + 1, k))
                myset.clear()
                break
            else:
                k += base

target.close()