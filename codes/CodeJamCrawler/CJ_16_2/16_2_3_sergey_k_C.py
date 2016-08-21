
import sys

def solve2(topics, groups, orig):
    res = 0
    if groups:
        first, other = groups[0], groups[1:]
        for topic in first:
            t = solve2(topics, other, orig + [topic])
            if t > res: res = t
    else:
        orig2 = set(x[1] for x in topics) - set(x[1] for x in orig)
        res = len(topics) - len(orig) - len(orig2)
    return res

def solve(topics):
    groups = {}
    for topic in topics:
        groups.setdefault(topic[0], []).append(topic)
    data = groups.values()
    return solve2(sum(data, []), data, [])

def main():
    T = int(sys.stdin.readline())
    for i in xrange(T):
        N = int(sys.stdin.readline())
        topics = [tuple(sys.stdin.readline().strip().split(' '))
                  for j in xrange(N)]
        print "Case #%d: %s" % (i + 1, solve(topics))

if __name__ == '__main__':
    main()
