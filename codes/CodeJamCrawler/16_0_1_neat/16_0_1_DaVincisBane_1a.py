
digits = []


def function(n, count):
    if n <= 0:
        print(("Case #" + str(count) + ": INSOMNIA"))
    else:
        digits = [False, False, False, False, False, False, False, False, False, False]
        factor = 1
        base = n
        while False in digits:
            #print(n)
            factor += 1
            for x in repr(n):
                x = int(x)
                digits[x] = True
                currentNumber = n
            n = base * factor
        print(("Case #" + str(count) + ": " + str(currentNumber)))
        return currentNumber


t = 0
with open("A-large.in", "r") as given:
    count = 0
    maxlines = 0
    for line in given:
        count = count + 1
        if count == 1:
            maxlines = int(line)
        elif count <= maxlines + 1:
            function(int(line), count - 1)



#function(1692, 1)