numCases = int(input())
for i in range(1,numCases+1):
    digits = list(range(10))
    n = int(input())
    output = 0
    if n == 0:
        print("Case #%i: INSOMNIA" % (i))
    else:
        increment = n
        while True:
            inputDigits = [int(d) for d in list(str(n))]
            for digit in digits:
                if digit in inputDigits:
                    digits[digit] = 10
            if sum(digits) == 100:
                output = n
                break
            n += increment
        print("Case #%i: %i" % (i, n))

