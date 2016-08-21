import string

T = int(input())
for t in range(T):
    d = dict()
    N = int(input())
    if N == 0:
        print("Case #" + str(t+1) + ": INSOMNIA")
    else:
        mul = 1
        while len(d) != 10:
            for c in str(N*mul):
                d[c] = 1
                if len(d) == 10:
                    print("Case #" + str(t+1) + ": " + str(N*mul))
                    break
            mul+=1

