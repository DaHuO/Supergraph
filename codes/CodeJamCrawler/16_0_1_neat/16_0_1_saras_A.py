def get_digits(N):
    return [int(d) for d in str(N)]

def merge_digits(current_digits, old_digits):
    new_digits = list(set(current_digits + old_digits))
    return new_digits

T = input()
for case in range(0,T):
    N = input()
    n = N
    ret = "INSOMNIA"
    if n:
        digits = merge_digits(get_digits(n),[])
        while True:
            # print digits
            ld = len(digits)
            if ld == 10:
                ret = n
                break
            n += N
            new_digits = merge_digits(get_digits(n), digits)
            nld = len(new_digits)
            # if nld == ld:
            #     print ": ", digits
            #     print ": ", new_digits
            #     break
            digits = new_digits
    output = "Case #%s: %s" % (case+1, ret)
    print output