def solve(x):
    if x == 0:
        return "INSOMNIA"
    digits = range(0, 10)
    x_curr = 0
    while digits:
        x_curr += x
        x_str = str(x_curr)
        i = 0
        while i < len(digits):
            if str(digits[i]) in x_str:
                digits.remove(digits[i])
            else:
                i += 1
    return x_curr

if __name__ == "__main__":
    filename = ("A")
    infile = open(filename + ".in.txt", "r")
    outfile = open(filename + ".out.txt", "w")

    lines = infile.read().strip().split("\n")
    cases = int(lines[0])

    lines = lines[1:]

    for i, l in enumerate(lines):
        val = int(l)
        res = solve(val)
        print >> outfile, "Case #" + str(i + 1) + ": " + str(res)

    infile.close()
    outfile.close()
