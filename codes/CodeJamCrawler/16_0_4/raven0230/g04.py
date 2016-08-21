T = eval(input())
for i in range(1,1+T):
    K, C, S = map(int,input().split())
    print("Case #{0}:".format(i), end='')
    for j in range(1,S+1):
        print(" {0}".format(j), end='')
    print()
        
