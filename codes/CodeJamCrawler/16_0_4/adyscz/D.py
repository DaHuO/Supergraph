import sys

if __name__ == '__main__':
    T = int(input())
    for t in range(1,T+1):
        K,C,S = map(int,sys.stdin.readline().split())
        if K == 1:
            print("Case #{}: {}".format(t, 1))
        elif C == 1:
            if S == K:
                print("Case #{}: {}".format(t, ' '.join(str(i) for i in range(1,K+1))))
            else:
                print("Case #{}: {}".format(t, "IMPOSSIBLE"))
        elif S + 1 < K:
            print("Case #{}: {}".format(t, "IMPOSSIBLE"))
        else:
            print("Case #{}: {}".format(t, ' '.join(str(i) for i in range(2,K+1))))
