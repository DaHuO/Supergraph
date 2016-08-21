import sys

def read_int():
    k = sys.stdin.readline().strip()
    return int (k)



def check_digits(n, marker):
    while n != 0:
        d = n % 10
        n = n / 10
        if marker["m"][d] == False:
            marker["c"] += 1;
            marker["m"][d] = True

def last_num(n):
    marker = {
        "m": [False]*10,
        "c": 0
    }

    res = 0
    while True:
        res+=n
        check_digits(res, marker)
        if marker["c"] == 10:
            return res
    

def main():
    c = read_int()
    for i in range(c):
        n = read_int()
        print "Case #%d: %s" % (i+1, last_num(n) if n != 0 else "INSOMNIA")


if __name__ == "__main__":
    main()
