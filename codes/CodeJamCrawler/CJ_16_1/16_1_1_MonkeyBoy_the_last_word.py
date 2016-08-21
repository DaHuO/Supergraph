
import sys
def read_string():
    return sys.stdin.readline().strip()

def read_int():
    k = sys.stdin.readline().strip()
    return int (k)



def ll(c):
    #return c
    l = [c, None]
    return (l, l)

def append((start, end), c):
    #return ll + c
    nend = [c, None]
    end[1] = nend
    return (start, nend)

def prepend((start, end), c):
    #return c + ll
    return ([c, start], end)

def to_str(l):
    r = ""
    while l != None:
        r =  r + l[0]
        l = l[1]
    return r
def last_word(s):
    r = ll(s[0])
    for c in s[1:]:
        if c < r[0][0]:
            r = append(r, c)
        else:
            r = prepend(r, c)
    return to_str(r[0])
        

def main():
    c = read_int()
    for i in range(c):
        n = read_string()
        print "Case #%d: %s" % (i+1, last_word(n))


if __name__ == "__main__":
    main()
