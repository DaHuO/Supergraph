import sys
import itertools
import math

class Jam:
    def __init__(self, value):
        self.value = value
        self.primes = []

    def __len__(self):
        return len(self.value)

    def __getitem__(self, i):
        return self.value[i]

    def __repr__(self):
        return self.value

    def __is_prime(self, n):
        if n == 2:
            return True
        elif n < 2 or not n & 1:
            return False
        for i in range(3, int(n**0.5)+1, 2):
            if n % i == 0:
                return False
        return True

    def __divisor_generator(self, n):
        large_divisors = []
        for i in xrange(1, int(math.sqrt(n) + 1)):
            if n % i == 0 and i*i != n and n / i != 1 and n != n / i:
                return n / i

    def __check_prime(self):
        for base in xrange(2, 11):
            base_int = int(self.value, base)
            if self.__is_prime(base_int):
                return True
        return False

    def is_jam(self):
        if not self[:1] == "1" or not self[-1:] == "1" or self.__check_prime():
            return False
        return True

    def get_legitimate(self):
        legitimate = []
        for base in xrange(2, 11):
            base_num = int(self.value, base)
            legitimate.append(self.__divisor_generator(base_num))
        return legitimate

def coin_jam(n, j, test_case):
    print "Case #%d:" % (test_case)

    prototype_jam_list = [Jam(''.join(str(x) for x in i)) for i in itertools.product([0, 1], repeat=n)]

    jam_list = []
    jam_counter = 0

    for prototype_jam in prototype_jam_list:
        if prototype_jam.is_jam():
            jam_list.append(prototype_jam)
        if len(jam_list) == j:
            break

    for i in xrange(j):
        print "%s %s" % (jam_list[i], ' '.join(str(n) for n in jam_list[i].get_legitimate()))

if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)

    t = int(f.readline())
    for _t in xrange(t):
        s = f.readline().split()
        coin_jam(int(s[0]), int(s[1]), _t+1)
