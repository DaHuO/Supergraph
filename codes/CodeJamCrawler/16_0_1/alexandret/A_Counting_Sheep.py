__author__ = 'Alexandret'

f = open('input.txt', 'r')
g = open('output.txt', 'w+')

# test = f.read()
tests = int(input())
for i in range(tests):
    num = int(input())
    ans = "INSOMNIA"
    if num > 0:
        k = 1
        digits = set()
        while len(digits) < 10:
            ans = num * k
            digits.update(str(ans))
            k += 1
    print("Case #", i+1, ": ", ans, sep='')
