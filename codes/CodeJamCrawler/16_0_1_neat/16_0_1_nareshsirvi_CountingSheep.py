
if __name__ == "__main__":
    T = input()
    for i in range(1, T + 1):
        N = input()
        if N == 0:
            print "Case #%d: INSOMNIA" % i
        else:
            seen = set()
            j = 1
            while True:
                seen.update(list(str(N * j)))
                if len(seen) == 10:
                    break
                j += 1

            print "Case #%d: %d" % (i, N * j)

