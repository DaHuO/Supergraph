# python 3.4 !!

#from functools import lru_cache
#@lru_cache(maxsize = None)
num_trials = int(input())

def convert_base_plus_one(b, digits):
    num = 0
    for i in digits:
        num = num * b + i
    return num + 1

def compute():
    K,C,S = map(int,input().split())
    needed_S = K // C + (K % C > 0) #ceil(K/C)

    if S < needed_S:
        return "IMPOSSIBLE"
    else:
        ans = ""
        for i in range(0, needed_S):
            start =  i * C
            end = (i+1)* C
            if end >= K:
                end = K
            ans = ans + str(convert_base_plus_one(K, list(range(start, end)))) + " "
            if end == K:
                break
        return str(ans)

for i in range (0, num_trials):
    print("Case #" + str(i+1) + ": " + compute())