def solve(N):
    answer = "INSOMNIA"
    multiplier = 0
    digits = [str(x) for x in xrange(0, 10)]

    if N is 0:
        return answer

    while len(digits) > 0:
        multiplier = multiplier + 1
        answer = N * multiplier

        for i in str(answer):
            if i in digits:
                digits.remove(i)

    return answer


T = int(raw_input())

for X in xrange(1, T + 1):
    N = int(raw_input())
    answer = solve(N)
    print "Case #{}: {}".format(X, answer)

