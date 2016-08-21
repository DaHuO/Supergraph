import prime

primes = prime.generate_primes(1000000)

def from_base(s, base):
    if (base == 10):
        return int(s)
    mult = 1
    result = 0
    for c in s[::-1]:
        result += int(c) * mult
        mult *= base
    return result



T = int(raw_input())

for t in xrange(1, T+1):
    temp = raw_input()
    N, J = [int(x.strip()) for x in temp.split()]
    solutions = {}
    for i in xrange(0, 2**(N-2)):
        s = '1' + format(i, '0%db' %(N-2)) + '1'
        temp_solution = []
        is_composite = True
        test_str = s
        for base in xrange(2, 11):
            n = from_base(s, base)
            factors = prime.prime_factor(n)
            if len(factors) == 1:
                is_composite = False
                break
            factor = factors[0][0]
            temp_solution.append(factor)
            test_str += ' ' + str(n)
        if not is_composite: 
            continue
        solutions[s] = temp_solution
        if len(solutions) >= J:
            break
    print('Case #%d:' %(t))
    for solution in solutions:
        solution_str = solution
        for factor in solutions[solution]:
            solution_str += ' ' + str(factor)
        print(solution_str)










