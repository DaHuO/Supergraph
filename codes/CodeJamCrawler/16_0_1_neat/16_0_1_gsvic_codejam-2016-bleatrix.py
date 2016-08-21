def numbers(n, digits):
    tmp = n
    while tmp > 0:
        last = tmp % 10
        if last not in digits:
            digits.add(last)
            if len(digits) == 10:
                return True
        tmp /= 10
    return False


def will_fall_asleep(n):
    digits = set()

    if n == 0:
        return 'INSOMNIA'
    i = 1
    while True:
        num = i*n
        sol = numbers(num, digits)
        if sol:
            return num
        i += 1


f = open('A-large.in').readlines()[1:]
o = open('output-A-large','w+')
for line, num in enumerate(f):
    res = will_fall_asleep(int(num))
    res = "Case #%d: %s\n"%(line+1, str(res))
    o.write(res)