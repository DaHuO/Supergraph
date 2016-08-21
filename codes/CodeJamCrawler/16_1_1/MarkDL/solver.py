def solve(problem):
    word = ""
    for c in problem:
        if c >= word[0:1]:
            word = c + word
        else:
            word += c
    return word

tests = int(raw_input())
for i in xrange(tests):
    problem = raw_input()
    answer = solve(problem)
    print "Case #{0}: {1}".format(i + 1, answer)
