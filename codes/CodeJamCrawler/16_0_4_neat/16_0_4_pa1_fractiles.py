def main():
    T = int(raw_input())
    for t in range(1, T + 1):
        K, C, S = raw_input().strip().split()
        K = int(K)
        C = int(C)
        S = int(S)
        p = K ** (C - 1)
        ans = ""
        for i in range(K):
            ans = ans + " " + str(i * p + 1)
        print "Case #{0}:{1}".format(t, ans)

if __name__ == "__main__":
    main()