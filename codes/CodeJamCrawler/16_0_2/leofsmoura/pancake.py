tests = int(raw_input())

for t in xrange(1, tests+1):
    answer = 0

    s = raw_input().strip()
    last = s[0]

    for c in s[1:]:
        if last == "+" and c == "-":
            answer += 1
        elif last == "-" and c == "+":
            answer += 1
        last = c
    if last == "-":
        answer += 1

    print "Case #{}: {}".format(t, answer)

