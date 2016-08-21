def main(n):
    d = [0] * 10
    # if n % 2 == 0:
    #     return run(d, 46, n)  # 45 is when 2 finds all digits
    # else:
    #     if n % 5 != 0:
    #         return run(d, 11, n)  # by 10 all odd numbers - { 5n } find all digits
    #     else:
    #         ans = run(d, 19, n)
    #         if ans == 'INSOMNIA' and d[9] == 0:
    #             s = 90
    #             while s % n is not 0:
    #                 s *= 10
    #             return s
    #         return ans
    return run(d, 1250, n)


def run(d, l, n):
    for i in range(1, l):
        m = n * i
        if track_digits(m, d) is 10:
            return m
    return 'INSOMNIA'


def track_digits(n, o):
    for d in str(n):
        o[int(d)] = 1
    return sum(o)


if __name__ == '__main__':
    t = int(raw_input())
    for index in range(0, t):
        num = int(raw_input())
        print 'Case #%d: %s' % (index + 1, main(num))
