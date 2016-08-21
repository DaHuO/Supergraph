
import itertools

digits = {
    "ZERO": 0,
    "ONE": 1,
    "TWO": 2,
    "THREE": 3,
    "FOUR": 4,
    "FIVE": 5,
    "SIX": 6,
    "SEVEN": 7,
    "EIGHT": 8,
    "NINE": 9,
}


def solve_problem(problem_row):
    found_numbers = []
    for digit, value in digits.iteritems():
        found = True
        iterator_letters = list(problem_row)
        while found:
            for c in digit:
                if c not in iterator_letters:
                    found = False
                    break
                else:
                    iterator_letters.remove(c)
            if found:
                found_numbers.append(digit)

    # print found_numbers

    found_combination = None
    for i in reversed(range(len(found_numbers) + 1)):
        if i == 0:
            continue
        for combination in itertools.combinations(found_numbers, i):
            iterator_letters = list(problem_row)
            try:
                letters_to_remove = [list(num) for num in combination]
                # print letters_to_remove
                map(iterator_letters.remove, itertools.chain(*letters_to_remove))
                if len(iterator_letters) == 0:
                    found_combination = combination
                break
            except Exception as e:
                pass

    found_combination = sorted([digits[i] for i in found_combination])
    return "".join([str(x) for x in found_combination])


def parse_problems():
    t = int(raw_input())  # read a line with a single integer
    problems = []
    for _ in xrange(1, t + 1):
        _raw_input = raw_input()
        problems.append(_raw_input)
    return problems


problem_rows = parse_problems()
solutions = map(solve_problem, problem_rows)
for counter, solution in enumerate(solutions):
    print "Case #{}: {}".format(counter+1, solution)
