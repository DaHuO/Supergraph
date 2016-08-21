def read_tuple():
    in_line = raw_input().strip().split(" ")
    return tuple(map(int, in_line))

def solve():
    k, c, s = read_tuple()
    if k > s:
        return "IMPOSSIBLE"
    size = pow(k, c)
    positions = list()
    for i in xrange(k):
        positions.append(i+1)
    return " ".join(map(str,positions))

def main():
    t = input()
    for i in xrange(1,t+1):
        ans = solve()
        print "Case #%d: %s" % (i, ans)

if __name__ == "__main__":
    main()
