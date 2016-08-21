alpha = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
for _ in range(int(input())):
    N = int(input())
    P = map(int, raw_input().split(' '))

    A = list()
    state = True
    while True and state:
        for i in range(len(P)):
            if P[i] == 0 :
                continue
            A.append(alpha[i])
            P[i] = P[i] - 1
            if sum(P) == 0:
                state = False
                break

    #print A
    print('Case #{}:'.format(_+1)),
    while(True):
        if len(A) <= N and len(A)%2 != 0:
            try:
                a = A.pop(len(A)-1)
                print a,
            except:
                continue

        else:
            try:
                a = A.pop(len(A)-1)
            except:
                break
            try:
                b = A.pop(len(A)-1)
                print a+b,
            except:
                print a,
                break

    print ''

