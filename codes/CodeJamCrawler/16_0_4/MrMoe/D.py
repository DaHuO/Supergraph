


T = int(input())

for t in range(T):
    
    K, C, S = tuple(map(int, input().split()))
    
    assert S == K
    
    print("Case #%d:" % (t+1), " ".join(map(str, range(1, S+1))))



