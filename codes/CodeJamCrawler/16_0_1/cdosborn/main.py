import sys

def digits(n, dict):
    while n > 0:
        dict[n % 10] = True
        n /= 10
    return dict

def main():
    sys.stdin.readline()
    task = 1
    for line in sys.stdin:
        i = 1    
        d = {}
        n = int(line)
        if n == 0:
            print "Case #%d: %s" % (task, "INSOMNIA")
            task += 1
            continue

        while len(d.keys()) < 10:
            digits(n * i, d)
            i += 1

        print "Case #%d: %d" % (task, n * (i - 1))
        task += 1

main()
