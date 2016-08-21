#!/usr/bin/env python
# -*- coding: utf-8 -*-
parties = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def solve(P):
    ans = []
    sum_all = sum(P)
    while sum_all != 0:
        # step = ""
        trial2 = P[:]
        ind1 = trial2.index(max(trial2))
        trial2[ind1] -= 1
        ind2 = trial2.index(max(trial2))
        trial2[ind2] -= 1
        sum_trial2 = sum_all - 2
        if sum_trial2==0 or all(x/float(sum_trial2) <= 0.5 for x in trial2):
            P[ind1] -= 1
            P[ind2] -= 1
            ans.append(parties[ind1] + parties[ind2])
            sum_all -= 2
            continue

        trial1 = P[:]
        ind = trial1.index(max(trial1))
        trial1[ind] -= 1
        sum_trial1 = sum_all - 1
        if sum_trial1==0 or all(x/float(sum_trial1) <= 0.5 for x in trial1):
            P[ind] -= 1
            ans.append(parties[ind])
            sum_all -= 1
            continue

        # for i in range(len(P)):
        #     if len(step) == 2:
        #         ans.append(step)
        #         sum_all -= 2
        #         break
        #
        #     if len(step) == 0:
        #         trial2 = P[:]
        #         trial2[i] -= 2
        #         sum_trial2 = sum_all - 2
        #         if all(x/float(sum_trial2) <= 0.5 for x in trial2):
        #             step = parties[i] + parties[i]
        #
        #     if len(step) < 2:
        #         trial1 = P[:]
        #         trial1[i] -= 1
        #         sum_trial1 = sum_all - 1
        #         if all(x/float(sum_trial1) <= 0.5 for x in trial1):
        #             step += parties[i]
        #
        # if len(step) != 0:
        #     ans.append(step)
        #     sum_all -= len(step)

    return " ".join(ans)

if __name__ == "__main__":
    testcases = int(input())

    for caseNr in xrange(1, testcases + 1):
        N = int(input())
        P = [int(x) for x in raw_input().split()]
        print("Case #%i: %s" % (caseNr, solve(P)))
