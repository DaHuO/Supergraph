import sys
in_file = sys.argv[1]
out_file = in_file + ".out"


def rev(x):
    if x == "+":
        return "-"
    return "+"

with open(in_file, "r") as fh, open(out_file, "w") as oh:
    t = int(fh.readline().replace("\n", ""))
    for k in xrange(t):
        s = fh.readline().replace("\n", "")
        if not s:
            break
        i = 0
        while True:
            if "-" not in s:
                break

            n = s.rfind("-")
            ns = ""
            for j, e in enumerate(s[:n+1]):
                ns += rev(s[j])
            s = ns + s[n+1:]
            i += 1

        oh.write("Case #%s: %s\n" % (k+1, i))
