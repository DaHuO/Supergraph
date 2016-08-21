t = int(raw_input())

def ans(n):
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        if n == 0:
                return "INSOMNIA"
        i = 0
        while len(digits) != 0:
                i = i+1
                k = n * i
                d = list(str(k))
                for x in d:
                        if x in digits:
                                digits.remove(x)
        return n * i

for i in xrange(1, t+1):
        n = int(raw_input())
        print "Case #{}: {}".format(i, ans(n))
