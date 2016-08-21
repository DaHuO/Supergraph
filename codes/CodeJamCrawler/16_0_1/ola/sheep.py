def one(n):
    d = [0]*10
    fact = 1
    while True:
        num = n*fact
        fact += 1 
        digs = [int(x) for x in str(num)]
        for i in digs:
            d[i] += 1
        if 0 not in d:
            return num
        if fact == 1000:
            return "INSOMNIA"

def solve(p):
    x = int(raw_input())
    print "Case #%d: %s" % (p, one(x))

if __name__ == "__main__":
    n = int(raw_input())
    for i in range(n):
         solve(i+1)
