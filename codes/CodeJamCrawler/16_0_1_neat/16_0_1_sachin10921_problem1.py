import sys

def get_last_number(n):
    numbers = set(map(str, range(10)))
    if n == 0:
        return "INSOMNIA"
    i = 0
    # import pdb
    # pdb.set_trace()
    while numbers:
        i +=1
        for x in str(n * i):
            numbers -= set(x)
    return n * i

def output(x, y):
    with open("output1.txt", 'a') as f:
        f.write("Case #" + str(x + 1) + ": " + str(y) + "\n")

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
        t = int(f.readline())
        for case in xrange(t):
            output(case, get_last_number(int(f.readline())))