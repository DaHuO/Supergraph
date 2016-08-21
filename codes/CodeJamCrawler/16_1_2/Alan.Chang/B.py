# python 3.4 !!

#from functools import lru_cache
#@lru_cache(maxsize = None)

num_trials = int(input())

def compute():
    N = int(input())
    a = [[]] * (2*N-1)
    for i in range(0, 2*N-1):
        a[i] = list(map(int,input().split()))
    
    missing = -1
    sorted_a = [[]] * N
    for i in range(0, N):
        a.sort(key=lambda x: x[i])
        if len(a) == 1 or a[0][i] != a[1][i]:
            assert missing == -1
            missing = i
            sorted_a[i] = [a[0]]
            a = a[1:]
        else:
            sorted_a[i] = [a[0], a[1]]
            a = a[2:]


    missing_one = [0] * N
    for i in range(N):
        if missing == i:
            missing_one[i] = sorted_a[missing][0][i]
        else:
            x = sorted_a[i][0][missing]
            y = sorted_a[i][1][missing]
            if x == sorted_a[missing][0][i]:
                missing_one[i] = y
            else:
                missing_one[i] = x

    return " ".join(str(x) for x in missing_one)

for i in range (0, num_trials):
    print("Case #" + str(i+1) + ": " + compute())
