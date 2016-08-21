from itertools import product

class JamCoin:

    def __init__(self, input_name):
        self.input_name = input_name
        self.validcoins = list()
        self.input()
        self.findcoins()
        self.output()

    def input(self):
        with open(self.input_name + '.in', 'r') as f:
            for i, l in enumerate(f):
                l = l.split('\n')[0]
                if i == 1:
                    self.N, self.J = [int(e) for e in l.split()]

    def output(self):
        output_name = 'output_' + self.input_name + '.out'
        with open(output_name, 'w') as f:
            f.write('Case #1: \n')
            for validcoin in self.validcoins:
                printline = str(''.join([str(e) for e in validcoin['digits']])) + ' '
                printline += ' '.join([str(e) for e in validcoin['divisors']]) + '\n'
                print(printline)
                f.write(printline)

    def evaluate_base_n(self, digits, base):
        evaluation = digits[0]
        for i in range(1, len(digits)):
            evaluation = base * evaluation + digits[i]
        return evaluation

    def findcoins(self):
        coins_found = 0
        for digits in product(*([[0, 1]]*(self.N-2))):
            digits = [1] + list(digits) + [1]
            if coins_found == self.J:
                break
            else:
                isvalidcoin = True
                base = 2
                divisors = list()
                while isvalidcoin and base < 11:
                    num = self.evaluate_base_n(digits, base)
                    divisor = self.get_divisor(num)
                    if divisor is None:
                        isvalidcoin = False
                    else:
                        divisors.append(divisor)
                    base += 1
                if isvalidcoin:
                    validcoin = dict()
                    validcoin['digits'] = digits
                    validcoin['divisors'] = divisors
                    self.validcoins.append(validcoin)
                    coins_found += 1

    def get_divisor(self, num):
        # Return the first non trivial divisor is one is found
        divisor = None
        for i in self.generator_primes(10000):
            if (num % i) == 0:
                divisor = i
                break
        return divisor

    def generator_primes(self, n):
        number = 2
        print(n)
        while number < n:
            if self.test_prime(number):
                yield number
            number += 1

    def test_prime(self, number):
        if number == 2:
            return True
        elif number % 2 == 0:
            return False
        else:
            for x in range(3, int(number**0.5 + 1), 2):
                if number % x == 0:
                    return False
        return True

if __name__ == '__main__':
    w = JamCoin('C-large')
