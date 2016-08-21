TRANSLATE = str.maketrans('+-', '-+')

def flip(cakes, i):
    #a = cakes
    b = cakes[:i][::-1].translate(TRANSLATE) + cakes[i:]
    #print(a, '->', b)
    return b

def func(cakes):
    a = cakes.find('+')
    b = cakes.find('-')
    c = 0
    while True:
        if ((a == 0) and (b == -1)):
            return c
        elif ((a == -1) and (b == 0)):
            cakes = flip(cakes, len(cakes))
        else:
            cakes = flip(cakes, max(a, b))
        a = cakes.find('+')
        b = cakes.find('-')
        c += 1

T = int(input())
for i in range(T):
    S = input()
    print('Case #{}: {}'.format(i+1, func(S)))
