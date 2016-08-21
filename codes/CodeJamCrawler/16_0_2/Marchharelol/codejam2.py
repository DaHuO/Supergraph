def canWin(s, count):
    start, end = 0, len(s) - 1
    while start < end:
        if s[start] == "+" and s[start + 1] == "-":
            count += 2

        start += 1

    return count + 1 if all_minus(s) else count

def all_minus(s):
    if s[0] != "-":
        return False

    return True

t = int(raw_input())

for i in xrange(1, t + 1):
    m = raw_input().split(" ")

    m[0] = canWin(m[0], 0)
    print "Case #{}: {}".format(i, m[0])
