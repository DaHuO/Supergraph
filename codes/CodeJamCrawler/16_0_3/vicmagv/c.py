from math import sqrt; from itertools import count, islice

filename = 'C-small-attempt0'

fi = open(filename+'.in', 'r')
fo = open(filename+'.out', 'w')
size = fi.readline()


def isPrime(n):
    if n < 2: return False
    for number in islice(count(2), int(sqrt(n)-1)):
        if not n%number:
            return number
    return 0

for case, line in enumerate(fi, start=1):
    fo.write('Case #{}: '.format(case) + '\n')
    (N, J) = line.strip().split()
    n_sol = 0
    for num in range(2**(int(N)-1)+1, 2**int(N), 2):
        numb = str(bin(num))[2:]
        sol = []
        sol.append(numb)
        for i in range(2,11):
            divisor = isPrime(int(numb, i))
            if divisor == 0:
                break
            sol.append(divisor)

        if len(sol) == 10:
            fo.write(' '.join([str(x) for x in sol]) + '\n')
            n_sol += 1
            print(n_sol)

        if n_sol == int(J):
            break
            print(n_sol, J)
