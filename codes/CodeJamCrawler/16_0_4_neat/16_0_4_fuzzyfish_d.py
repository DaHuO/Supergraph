
T = int(input())

for ttt in range(T):
    K, C, S = map(int, input().split())
    ans = list(range(1, S+1))
    
    ans = [str(i) for i in ans]
    print("Case #%d: " % (ttt+1) + " ".join(ans))
