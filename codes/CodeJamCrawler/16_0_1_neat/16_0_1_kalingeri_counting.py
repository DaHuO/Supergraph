def get_digits(s):
    return list(set([i for i in s]))

def check(l):
    l = [int(i) for i in l]
    l.sort()
    return l == range(10)

cases = int(raw_input())
for case in range(cases):
    n = int(raw_input())
    digits = get_digits(str(n))
    if n == 0:
        output = "INSOMNIA"
    else:
        i = 2
        while check(digits) is False:
            digits = get_digits(str(n * i) + ''.join(digits))
            i += 1
        output = str((i - 1) * n)
            
    print "Case #%i:"%(case + 1), output
