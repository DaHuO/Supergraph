def findLastNum(n):
    i = 1
    hasSeen = [False for _ in range(10)]
    cur = "INSOMNIA"
    if n == 0:
        return cur
    while False in hasSeen:
        cur = i*n
        for ch in str(cur):
            hasSeen[int(ch)] = True
        i += 1
    return cur

def main():
    T = int(raw_input())
    for i in range(T):
        N = int(raw_input())
        lastNum = findLastNum(N)
        print "Case #" + str(i+1) + ": " + str(lastNum)
main()
