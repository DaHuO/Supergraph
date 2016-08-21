t = int(input())

def get_digits(n):
    digits = []
    while n > 0:
        digits.append(n%10)
        n = n//10
    return set(digits)


for caseid in range(1, t+1):
    n = int(input())
    if n == 0:
        print("Case #%s: %s" % (caseid, "INSOMNIA"))
    else:
        digits = set([])
        for i in range(1, 1000):
            for d in get_digits(i*n):
                digits.add(d)
            if digits == set(range(0, 10)):
                print("Case #%s: %s" % (caseid, n*i))
                break
            

