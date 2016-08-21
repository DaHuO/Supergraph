import sys

def output(K, C, S):
    #if K == 1:
    #    return "1"
    return " ".join(map(str, range(1, K + 1)))

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for t in range(T):
        K, C, S = map(int, sys.stdin.readline().strip().split(" "))
        answer = output(K, C, S)
        print "Case #%d: %s" % (t + 1, answer)
