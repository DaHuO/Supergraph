t = int(raw_input())

for i in xrange(1, t + 1):
    n = int(raw_input())
    case_str = "Case #{}: {}"
    if n == 0:
        print case_str.format(i, "INSOMNIA")
    else:
        digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        k = 0
        while digits:
            k += n
            m = k
            while m != 0:
                digit = m % 10
                if digit in digits:
                    digits.remove(digit)
                if not digits:
                    print case_str.format(i, k)
                    break
                m /= 10
