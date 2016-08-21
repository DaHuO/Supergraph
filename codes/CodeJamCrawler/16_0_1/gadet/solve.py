import sys

data = sys.stdin.read()
numbers = map(int, data.split('\n')[1:-1])
for index, num in enumerate(numbers, start=1):
    if num == 0:
        print "Case #%s: INSOMNIA" % index
    else:
        digits = {}
        cur = num
        while len(digits) < 10:
            for digit in str(cur):
                digits[digit] = True
            cur += num
        print "Case #%s: %s" % (index, cur - num)
