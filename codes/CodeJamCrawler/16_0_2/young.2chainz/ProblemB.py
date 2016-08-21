def reverse(arr, n):
    for i in range(n):
        if arr[i] == "-":
            arr[i] = "+"
        else:
            arr[i] = "-"
    return arr

def solve(arr, n):
    if n == 0:
        return 0
    if arr[n-1] == '-':
        return 1 + solve(reverse(arr, n), n - 1)
    else:
        return solve(arr, n - 1)

if __name__ == "__main__":
    filename = ("B")
    infile = open(filename + ".in.txt", "r")
    outfile = open(filename + ".out.txt", "w")

    lines = infile.read().strip().split("\n")
    cases = int(lines[0])

    lines = lines[1:]

    for i, l in enumerate(lines):
        val = list(l)
        res = solve(val, len(val))
        print >> outfile, "Case #" + str(i + 1) + ": " + str(res)

    infile.close()
    outfile.close()
