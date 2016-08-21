class Solution:

    def number_to_base(self, n, b):
        if n == 0:
            return [0]
        digits = []
        while n:
            digits.append(int(n % b))
            n /= b
        return digits[::-1]

    def binary_to_num(self, digits, base):
        d = list(reversed(digits))
        num = 0
        for i in range(len(d)):
            if d[i] == 1:
                num += pow(base, i)
        return num

    def is_prime(self, n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i+2) == 0:
                return False
            i = i + 6
        return True

    # return -1 for prime
    def get_divisor(self, n):
        if n <= 1:
            return 1
        elif n <= 3:
            return -1
        elif n % 2 == 0:
            return 2
        elif n % 3 == 0:
            return 3
        i = 5
        while i * i <= n:
            if n % i == 0:
                return i
            elif n % (i+2) == 0:
                return i+2
            i = i + 6
        return -1

    def pow(self, base, n):

        if n == 0:
            return 1
        if n % 2 == 0:
            p = self.pow(base, n/2)
            return p * p
        else:
            p = self.pow(base, (n-1)/2)
            return base * p * p

    def process(self, case, N, J):
        print "Case #%d:" % case

        mid = N - 2
        max = self.pow(2,mid)
        i = 0
        count = 0
        while i < max and count < J:

            digits = self.number_to_base(i, 2)
            while len(digits) < mid:
                digits = [0] + digits
            digits = [1] + digits + [1]

            no_prime = True
            divisors = []
            for base in range(2,11):
                num = self.binary_to_num(digits, base)

                divisor = self.get_divisor(num)
                if divisor < 1:
                    no_prime = False
                    break
                divisors.append(divisor)

            if no_prime:
                s = ""
                for c in digits:
                    s += str(c)
                for d in divisors:
                    s += ' ' + str(d)
                print s
                count += 1

            i += 1

T = int(raw_input())
for i in xrange(T):
    line = raw_input()
    N, J = [int(n) for n in line.split()]
    s = Solution()
    s.process(i+1, N, J)