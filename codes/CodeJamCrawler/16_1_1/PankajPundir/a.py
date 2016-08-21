import sys
in_file = sys.argv[1]
out_file = in_file + ".out"
with open(in_file, "r") as fh, open(out_file, "w") as oh:
    t = int(fh.readline().replace("\n", ""))
    for k in xrange(t):
        s = fh.readline().replace("\n", "")
        ans = s[0]
        for e in s[1:]:
            if e >= ans[0]:
                ans = e + ans
            else:
                ans += e

        oh.write("Case #" + str(k + 1) + ": " + ans + "\n")

