import fileinput
import itertools
import string

flip_map = string.maketrans("+-","-+")

def flip_str(s):
    return "".join(reversed(string.translate(s,flip_map)))

def solve(s):
    if s.find("-") == -1:
        return 0
    if s[0] == "+":
        for i in itertools.count(1):
            if s[i] == "-":
                sub_s = s[:i]
                return solve(flip_str(sub_s)+s[i:])+1
    else:
        for i in range(1,len(s)):
            if s[i] == "+":
                sub_s = s[:i]
                return solve(flip_str(sub_s)+s[i:])+1
        return solve(flip_str(s))+1
def main():
    it = fileinput.input()
    it.next()
    for i,l in enumerate(it,1):
        print "Case #%d: %d" % (i,solve(l.strip()))

if __name__ == "__main__":
    main()
