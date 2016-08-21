infile = open("A-large.in", "r")

def solve(line):
    N = int(line)
    if N == 0:
        return "INSOMNIA"
    missing = list(range(10))
    last = 0
    for x in range(1, 10**16):
        i = x*N
        my_missing = missing
        for y in missing[:]:
            if str(y) in str(i):
                missing.remove(y)
        last = i
        if len(missing) == 0:
            break
    else:
        return "INSOMNIA"
    return str(last)

def main():
    count = int(infile.readline())
    for x in range(count):
        print("Case #" + str(x + 1) + ": " + str(solve(infile.readline())))

if __name__ == "__main__":
    main()