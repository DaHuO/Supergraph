import fileinput
import itertools

def solve(N):
    seen = set()
    if N == 0:
        return "INSOMNIA"
    for i in itertools.count(1):
        s = str(N*i)
        seen.update(set(s))
        if len(seen) == 10:
            return s
        if i > 1000000:
            return "INSOMNIA"

def main():
    it = fileinput.input()
    l = it.next()
    for i,l in enumerate(it,1):
        print "Case #%d: %s" % (i,solve(int(l)))

if __name__ == "__main__":
    main()
