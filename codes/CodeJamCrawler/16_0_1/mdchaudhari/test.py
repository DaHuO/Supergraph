from collections import defaultdict

def update_digits(n):
    for x in [x for x in str(n)]:
        digits[x] += 1

global digits

with open('input.txt') as f:
    t = int(f.readline())
    for i in range(1, t+1):
        digits = defaultdict(int)
        n = int(f.readline())
        if n == 0:
            print "Case #{0}: INSOMNIA".format(i)
        else:
            counter = 2
            update_digits(n)
            while len(digits) < 10:
                update_digits(n * counter)
                counter += 1
            print "Case #{0}: {1}".format(i, n * (counter - 1))