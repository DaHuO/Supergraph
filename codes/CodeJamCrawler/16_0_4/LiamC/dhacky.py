from itertools import product, combinations
t = int(input())
# t = 1
for case in range(1,t+1):
    k,c,s = map(int,input().split())
    # k, c, s = 2, 3, 2
    ans = ' '.join(map(str,range(1,k+1)))

    print ("Case #{}: {}".format(case, ans))
