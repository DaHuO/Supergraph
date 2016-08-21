import fileinput

def place_letter(s,c):
    if ord(s[0]) > ord(c):
        return s+c
    return c+s

def solve(o):
    s = o[0]
    for c in o[1:]:
        s = place_letter(s,c)
    return s

def main():
    it = fileinput.input()
    n = it.next()
    for i,l in enumerate(it,1):
        print "Case #%d: %s" % (i,solve(l.strip()))

if __name__ == "__main__":
    main()
