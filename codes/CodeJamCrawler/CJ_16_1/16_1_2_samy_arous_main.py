from pygraph.classes.graph import graph
from collections import Counter


def solve(n, lists):
    c = Counter()
    for i, row in enumerate(lists):
        c.update(row)
    missing = [h for h, v in c.items() if v % 2]
    return sorted(missing)



def read_input():
    n = int(raw_input())
    lists = [
        map(int, raw_input().strip().split())
        for _ in range(2*n-1)
    ]
    return n, lists

if __name__ == '__main__':
    t = int(raw_input())
    for i in range(t):
        res = map(str, solve(*read_input()))
        print "Case #%s: %s" % ( i+1, " ".join(res) )

    # test_cases = [
    #     (3, [[1,2,3], [2,3,5], [3,5,6], [2,3,4], [1,2,3]])
    # ]
    # for i, test in enumerate(test_cases):
    #     res = map(str, solve(*test))
    #     print "Case #%s: %s" % ( i+1, " ".join(res) )