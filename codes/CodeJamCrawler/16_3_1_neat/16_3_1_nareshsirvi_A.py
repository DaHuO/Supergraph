import string

if __name__ == "__main__":
    D = {i: c for i, c in enumerate(string.ascii_uppercase)}

    T = input()
    for i in range(1, T + 1):
        N = input()
        P = map(int, raw_input().split())
        plan = []
        while True:
            max_i, smax_i = 0, 0
            for j in range(len(P)):
                if P[max_i] < P[j]:
                    max_i = j

            if max_i == 0:
                smax_i = 1
            for j in range(len(P)):
                if j != max_i and P[smax_i] < P[j]:
                    smax_i = j

            P[max_i] -= 1
            P[smax_i] -= 1
            if (max(P) <= sum(P) / 2):
                plan.append(D[max_i] + D[smax_i])
            else:
                P[smax_i] += 1
                plan.append(D[max_i])

            # print P
            if True not in [x != 0 for x in P]:
                break

        print "Case #%d: %s" % (i, " ".join(plan))

