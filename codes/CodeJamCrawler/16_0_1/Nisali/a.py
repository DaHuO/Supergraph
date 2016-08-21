def solution(n):
    if n == 0:
        return "INSOMNIA"
    criteria = set("0123456789")
    digits_seen = ""
    i = 1
    while True:
        digits_seen = str(digits_seen) + str(n*i)
        if set(digits_seen) == criteria:
            break
        i += 1
    return i*n

infile = open("l.in", "r")
outfile = open("lout.in", "w")

n = infile.readline()
n = int(n)

for i, line in enumerate(infile):
    line = line.strip()
    n = int(line)
    print("Case #{}: {}".format(i+1, solution(n)))
    outfile.write("Case #{}: {}\n".format(i+1, solution(n)))
