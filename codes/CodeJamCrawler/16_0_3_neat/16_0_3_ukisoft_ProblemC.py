

class JamCoin(object):
    _non_trivial_divisors = {1: False, 2: False}

    @classmethod
    def transfer(cls, target, l):
        _target = bin(target)[2:]
        if len(_target) < l:
            zero = ''
            for _ in range(l - len(_target)):
                zero += '0'
            _target = zero + _target
        return _target

    @classmethod
    def get_non_trivial_divisor(cls, target):
        if target in cls._non_trivial_divisors:
            return cls._non_trivial_divisors[target]
        for j in range(2, 1000):
            if target % j == 0:
                cls._non_trivial_divisors[target] = j
                return j
        return False


def solve():
    for _ in range(int(input())):
        print('Case #' + str(_ + 1) + ':')
        inputs = input().split(' ')
        N = int(inputs[0])
        J = int(inputs[1])
        _max_len = ''
        for __ in range(N - 2):
            _max_len += '1'
        now = 0
        J_count = 0
        while now <= int(_max_len, 2) and J_count < J:
            jamcoin = '1' + JamCoin.transfer(now, N - 2) + '1'
            _result = [jamcoin]
            for base in range(2, 11):
                _non_trivial_divisor = JamCoin.get_non_trivial_divisor(int(jamcoin, base))
                if _non_trivial_divisor is False:
                    break
                _result.append(str(_non_trivial_divisor))
            if len(_result) > 9:
                print(' '.join(_result))
                J_count += 1
            now += 1


if __name__ == '__main__':
    solve()
