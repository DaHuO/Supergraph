

def countingSheep():
    t = int(raw_input())
    for i in xrange(1, t + 1):
        n = int(raw_input())
        if n <= 0:
            print "Case #{}: {}".format(i, "INSOMNIA")
            continue
        seen = [False] * 10
        x = n
        for j in map(int, str(x)):
            seen[j] = True
        while seen.count(True) != 10:
            x += n
            for j in map(int, str(x)):
                seen[j] = True
        print "Case #{}: {}".format(i, x)


if __name__ == "__main__":
    countingSheep()
