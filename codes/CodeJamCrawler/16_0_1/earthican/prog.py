checks = {}
digits = []
sheep = {}

needed = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

def track_digits(s):
    digits_check = {}
    ret = []
    for c in s:
        if c not in digits_check:
            digits_check[c] = True
            ret.append(c)
    return ret

def calc_sheep(n):
    [digits.append(d) for d in track_digits(str(n))]
    if all(c in digits for c in needed):
        return n
    else:
        return None

def main(N):
    i = 1
    while True:
        curr = i * N
        if curr in sheep:
            return 'INSOMNIA'
        else:
            sheep[curr] = curr
        res = calc_sheep(curr)
        if res:
            return res
        i = i + 1

if __name__ == '__main__':
    T = int(raw_input())
    for i in range(1, T+1):
        N = int(raw_input())
        print 'Case #%d:' % i, main(N)
        checks.clear()
        sheep.clear()
        digits[:] = []