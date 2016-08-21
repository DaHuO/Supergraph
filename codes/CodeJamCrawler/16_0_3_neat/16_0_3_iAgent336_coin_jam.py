def solve(single_case):
    case = single_case.split(' ')
    #print case
    N = int(case[0])
    J = int(case[1])
    answers = []
    for n in range(2**(N-1)+1, 2**N, 2):
        n_str = int2base(n,2)
        #print n_str
        divisors = []
        for b in range(2,11):
            d = get_divisor(int(n_str,b))
            if d == 0: break
            else: divisors.append(d)
        else: # if the inner loop ends normally
            #print divisors
            answers.append(' '.join([n_str] + map(str, divisors)))
            J -= 1
            if J <= 0: break
        continue

    return '\n'.join(answers)

def get_divisor(n): # return 0 if n is a prime
    if n==2:
        return 0
    if n & 1 == 0:
        return 2
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return i
    else:
        return 0

def int2base(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n /= b
    return ''.join(map(str, digits[::-1]))

def main():
    testcases = input()
    for case_num in xrange(1, testcases+1):
        single_case = raw_input()
        print("Case #%i:\n%s" % (case_num, solve(single_case)))

if __name__=='__main__':
    main()


