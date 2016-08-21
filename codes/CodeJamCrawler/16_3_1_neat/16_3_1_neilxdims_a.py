import sys, traceback
sys.setrecursionlimit(5000)

def lim(n):
    return n//2


def solution(N, a):
    P = []
    for i, p in enumerate(a):
        P.append([p, chr(i+65)])

    rem = sum(a)

    ans = []
    while rem > 0:
        P = sorted(P, reverse=True)
        if rem == 3:
            P[0][0] -= 1
            ans.append(P[0][1])
            rem -= 1
        else:
            if P[0][0] == P[1][0]:
                P[0][0] -= 1
                P[1][0] -= 1
                rem -= 2
                ans.append(P[0][1] + P[1][1])
            else:
                P[0][0] -= 2
                rem -= 2
                ans.append(P[0][1] + P[0][1])
    return ans

######### main
t = int(input())
for i in range(1, t + 1):
    N = int(input())
    a = [int(i) for i in input().split(' ')]
    print("Case #{}: ".format(i), end='')
    print(' '.join(solution(N, a)))
    # try:
    #     print(solution(N, bffof))
    # except Exception as ex:
    #     # print(type(ex).__name__, ex.args)
    #     traceback.print_exc()


