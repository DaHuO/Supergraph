from lenstra import lenstra
from sys import stdin

def representation(bitmask, size, base):
    rep = 0
    for i in range(size):
        # getting (i+1)-th bit from the end
        d = (bitmask >> i) & 1
        rep += d * base**i

    return rep

def to_string(bitmask, size):
    s = ''
    for i in range(size):
        s = str((bitmask >> i) & 1) + s
    return s


def find(size, number):
    counter = 0
    for x in range(2**(size-2)):
        bitmask = (1 << (size-1)) + (x << 1) + 1
        
        div = [0] * 9
        doesnt_fit = False

        for base in range(2, 11):
            n = representation(bitmask, size, base)
            d = lenstra(n, 1000)
            if d == False:
                doesnt_fit = True
                break
            div[base-2] = d

        if doesnt_fit: 
            continue

        counter += 1
        print('%s' % (to_string(bitmask, size) + ' ' + ' '.join([str(d) for d in div])))
        if counter >= number:
            break


T = int(stdin.readline())
for t in range(T):
    s = stdin.readline().split()
    n = int(s[0])
    j = int(s[1])

    print('Case #%d:' % (t+1, ))
    find(n, j)

