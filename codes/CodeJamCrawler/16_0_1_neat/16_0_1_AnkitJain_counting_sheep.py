
def get_last_no(n):
    digits = set()
    count = 1

    if n == 0:
        return "INSOMNIA"

    actual_n = n
    while count:
        temp = n
        while temp > 0:
            x = temp%10
            digits.add(x)
            temp /= 10

        if len(digits) == 10:
            return n

        count += 1
        n = actual_n * count


T = int(raw_input())

for i in range(T):
    n = int(raw_input())
    print "Case #%s: %s" % (str(i+1), str(get_last_no(n)))