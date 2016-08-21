import numpy as np
import string
def solve(N, distribution, parties):
    # assume we lost a column list
    #print N
    #print distribution
    #print parties
    total = sum(distribution)
    plan = []
    while total > 2 and sum(distribution[:]>0)>2:
        p1 = np.argmax(distribution)
        if distribution[p1] > total-distribution[p1]:
            print 'ERROR'
            print parties[p1]
            print distribution
        distribution[p1] -= 1
        plan.append(str(parties[p1]))
        total = sum(distribution)
    while total > 0:
        pair = ''
        p1 = np.argmax(distribution)
        if distribution[p1] > total-distribution[p1]:
            print 'ERROR'
            print parties[p1]
            print distribution
        for i in range(len(distribution)):
            if distribution[i] > 0:
                pair += str(parties[i])
                distribution[i] -= 1
        plan.append(pair)
        total = sum(distribution)
    return ' '.join(plan)

def main():
    testcases = input()
    for case_num in xrange(1, testcases+1):
        N = int(raw_input())
        distribution = raw_input().split(' ')
        distribution = np.array(distribution).astype(int)
        parties = {}
        for i in xrange(N):
            parties[i] = string.ascii_uppercase[i]
        print("Case #%i: %s" % (case_num, solve(N, distribution, parties)))

def test():
    single_case = raw_input()
    print("Case #1: %s" % (solve(single_case)))


if __name__=='__main__':
    main()
    #test()

