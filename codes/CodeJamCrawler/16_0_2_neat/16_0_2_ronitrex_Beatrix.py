def flip(N):
    global i
    if '-' not in N:
        return
    if '+' not in N:
        i+=1
        return

    if N[0]== '-':
        x = N.index('+')
        NewN = N[:x]
        OldN = N[x+1:]
        NewN = NewN.replace('-','+')
        N = NewN+OldN
        # print(NewN, OldN, N, 'Craft')
        # print(N)
        i += 1
        flip(N)

    elif N[0]== '+':
        x = N.index('-')
        NewN = N[:x]
        OldN = N[x+1:]
        NewN = NewN.replace('+','-')
        N = NewN + OldN
        # print(NewN, OldN, N, 'Fair')
        # print(N)
        i+=1
        flip(N)


T = int(input())
for _ in range(1, T+1):
    N = input()
    i=0
    flip(N)
    print('Case #{}: {}'.format(_, i))


