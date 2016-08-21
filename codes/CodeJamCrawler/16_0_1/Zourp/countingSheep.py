def get_digits(num, digits):
    l = [int(d) for d in str(num)]

    for i in range(len(l)):
        digits[l[i]] = l[i]

    return digits

nb_tests = int(input())

for t in range(1, nb_tests + 1):
    n = int(input())
    digits = [-1 for i in range(10)]

    if n == 0:
        print("Case #%d: INSOMNIA" % t)
    else:
        i = 1
        num = n
        while -1 in digits:
            num = n * i
            digits = get_digits(num, digits)
            i +=1
        print("Case #%d: %d" % (t, num))
