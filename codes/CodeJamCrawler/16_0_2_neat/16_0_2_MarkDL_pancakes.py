def flip(problem, i):
    for x in xrange(i):
        problem[x] = '-' if problem[x] == '+' else '+'
    j = 0
    k = i - 1
    while j < k:
        problem[j], problem[k] = problem[k], problem[j]
        j += 1
        k -= 1
    return problem

def solve(problem):
    problem = list(problem)
    flips = 0
    while True:
        while problem[-1] == '+':
            problem = problem[:-1]
            if len(problem) == 0:
                return flips
        if problem[0] == '-':
            problem = flip(problem, len(problem))
            flips += 1
        else:
            problem = flip(problem, problem.index('-'))
            flips += 1
    return flips

tests = int(raw_input())
for i in xrange(tests):
    problem = raw_input()
    answer = solve(problem)
    print "Case #{0}: {1}".format(i + 1, answer)
