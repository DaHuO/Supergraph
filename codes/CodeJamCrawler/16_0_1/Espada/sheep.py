def run():
    x = input()
    for i in range(x):
        T = input()
        print 'Case #%d: %s' % (i+1, calculate_N(T))

def calculate_N(T):
    if T == 0:
        return 'INSOMNIA'
    else:
        digits = set()
        n = 1
        new_T = T
        while True:
            new_T = T * n
            n += 1
            t = new_T
            while t:
                digit = t % 10
                digits.add(digit)
                t //= 10
                if len(digits) == 10:
                    return new_T


run()
