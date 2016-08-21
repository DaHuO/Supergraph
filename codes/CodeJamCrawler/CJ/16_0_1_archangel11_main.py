filename = "a.in"
outfilename = "output.txt"

def solve(f):
    output = 0
    n = int(f.readline().strip())
    if n == 0:
        return "INSOMNIA"

    seen = set(str(n))
    number = n
    while len(seen) < 10:
        number += n
        seen.update(set(str(number)))
    return number

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
