import sys
from collections import deque

digits = [ "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" ]
def search(S):

    def count(dstr):
        charcnt = [0] * 26
        for c in dstr:
            i = ord(c) - ord('A')
            charcnt[i] += 1
        return charcnt
    
    def vminus(v, u):
        if any(i < j for i, j in zip(v, u)):
            return False
        return [i - j for i, j in zip(v, u)]

    digitcnt = [None] * 10
    for i, d in enumerate(digits):
        digitcnt[i] = count(d)
    scnt = count(S)
    q = deque([(0, scnt, [])])
    while q:
        n, cnt, seq = q.popleft()
        if sum(cnt) == 0:
            return seq
        if n > 9:
            continue
        if n < 9:
            q.append((n+1, list(cnt), list(seq)))
        while cnt:
            cnt = vminus(cnt, digitcnt[n])
            if cnt:
                seq.append(n)
                q.append((n+1, list(cnt), list(seq)))

def main():
    T = int(sys.stdin.readline())
    for t in range(1, T+1):
        S = sys.stdin.readline().strip()
        seq = search(S)
        print "Case #%d:" % t, "".join(map(str, seq))

if __name__ == "__main__":
    main()
