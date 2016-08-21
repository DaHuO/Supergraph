import sys, functools

def lw(s):
    last = s[0]

    for i in s[1:]:
        if i >= last[0]:
            last = i + last
        else:   
            last = last + i
    return last

if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)

    T = int(f.readline())

    for i in range(T):
        S =  f.readline().strip()
        print("Case #{0}: {1}".format(i + 1, lw(S)))