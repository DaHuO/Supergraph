filename = "a.in"
outfilename = "output.txt"

def solve(f):
    output = 0
    k, c, s = map(int, f.readline().split())
    ans = []
    if s < (k + c - 1) / c:
        return "IMPOSSIBLE"
    multipliers = [pow(k, i) for i in range(min(k,c)-1, -1, -1)]
    i = 0
    mi = 0
    current = 0
    while i < k:
        if mi < len(multipliers):
            current += multipliers[mi] * i
        else:
            ans.append(current + 1)
            current = 0
            i -= 1
            mi = -1
        mi += 1
        i += 1
    ans.append(current + 1)

    return " ".join(map(str, ans))

def out(s, o):
    print s
    o.write("{}\n".format(s))

def main():
    f = open(filename)
    o = open(outfilename, 'w+')
    T = int(f.readline())
    t = 1
    while t <= T:
        output = solve(f)
        out("Case #{}: {}".format(t, output), o)
        t+=1

if __name__ == "__main__":
    main()
