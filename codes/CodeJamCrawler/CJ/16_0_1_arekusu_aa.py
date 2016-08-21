import sys

def checkNumber(n):
    if n == 0:
        return "INSOMNIA"
    else:
        info = set()
        i = 1
        m = n
        while True:
            m = n * i
            ret = m
            while m > 0:
                p = m%10
                if p not in info:
                    info.add(p)
                m = m/10
            i += 1
            if len(info) == 10:
                return str(ret)

def sleep(filename):
    file = open(filename)
    file.readline()
    i = 0
    for line in file:
        i += 1
        if line.strip() == "":
            continue
        r = checkNumber(int(line))
        print "Case #%d: %s" % (i, r)

if __name__ == "__main__":
    sleep(sys.argv[1])
