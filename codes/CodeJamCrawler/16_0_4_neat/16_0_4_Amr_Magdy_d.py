T = int(raw_input())
for case in range(T):
    K, C, S = map(int, raw_input().strip().split())
    if (K / 2) > S or ( C == 1 and S < K ):
        print "Case #{}: {}".format(case+1, "IMPOSSIBLE")
    elif C == 1:
        sol = []
        for i in range(K):
            sol.append(str(i+1))
        print "Case #{}: {}".format(case+1, " ".join(sol))


    else:
        step_length = K**(C-1)
        inner = (step_length / K)
        sol = []
        for i in range(0, K, 2):
            if K % 2 == 0 or i != K-1:
                shift = (step_length / K) * (i+1) + 1
                sol.append(str(step_length*i + shift))
            else:
                sol.append(str(step_length*i + inner))


        print "Case #{}: {}".format(case+1, " ".join(sol))
