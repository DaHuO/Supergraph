import itertools

def report_answers(answers):
    print 'Case #1:'
    for answer in answers:
        jamcoin, divisors = answer
        print('{} {}'.format(jamcoin, ' '.join(map(str, divisors))))

def try_small_factors(num):
    for x in xrange(2, 30):
        if num % x == 0:
            return x

def get_soln(N, J):
    answers = []
    for combo in itertools.product(['0', '1'], repeat=N-2):
        combo = list(combo)
        combo.append('1')
        combo.insert(0, '1')
        combo = ''.join(combo)

        factors = []
        for b in xrange(2, 11):
            num = int(combo, b)
            found_factor = try_small_factors(num)
            if not found_factor:
                break
            else:
                factors.append(found_factor)

        if len(factors) < 9:
            continue
        else:
            answers.append((combo, factors))

        if len(answers) == J:
            return answers

    return answers

N = 32
J = 500
answers = get_soln(N, J)
report_answers(answers)
