import sys
in_file = sys.argv[1]
out_file = in_file + ".out"
with open(in_file, "r") as fh, open(out_file, "w") as oh:
    t = int(fh.readline().replace("\n", ""))
    for k in xrange(t):
        try:
            n = int(fh.readline().replace("\n", ""))
        except ValueError:
            break
        l = []
        done = False
        for i in xrange(1, 1000):
            y = i * n
            for e in str(y):
                if e not in l:
                    l.append(e)
                if len(l) == 10:
                    oh.write("Case #" + str(k+1) + ": " + str(y) + "\n")
                    done = True
                    break
            if done:
                break
        if not done:
            oh.write("Case #" + str(k+1) + ": " + "INSOMNIA\n")
