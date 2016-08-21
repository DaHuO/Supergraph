import fileinput

# We needn't handle the 0 case correctly because it is always INSOMNIA
def digits(num):
    result = set()
    while (num > 0):
        digit = num % 10
        result.add(digit)
        num = num / 10
    return result

lines = map(int, [l for l in fileinput.input()])
for t, N in enumerate(lines[1:]):
    answer = "INSOMNIA"
    if N == 0:
        print "Case #%i: INSOMNIA" % (t + 1)
        continue
    num = 0;
    seen = set()
    while True:
        num += N
        seen = seen.union(digits(num))
        # print seen
        if len(seen) == 10:
            answer = num
            break;
    print "Case #%i:" % (t + 1), answer
