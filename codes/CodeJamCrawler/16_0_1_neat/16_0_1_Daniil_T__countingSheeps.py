for test in range(input()):
    print "Case #%d:" % (test+1),
    N = input()

    if N == 0:
        print "INSOMNIA"
    else:
        count = 0
        seen = [False for i in range(10)]
        currentNumber = N

        while True:
            x = currentNumber
            while x > 0:
                digit = x % 10
                x //= 10
                if not seen[digit]:
                    count += 1
                    seen[digit] = True
            if count == 10:
                break
            currentNumber += N

        print currentNumber
