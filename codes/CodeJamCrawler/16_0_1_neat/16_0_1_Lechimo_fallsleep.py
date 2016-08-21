def lastNumber(n):
    digits = ""
    i = 1
    while ''.join(digits) != "0123456789":
        m = i * n
        number = str(m)
        for j in number:
            if  j not in digits:
                digits += j
                digits = sorted(digits)
        i += 1
    return m

t = int(input())

for i in range(1, t + 1):
    n = int(input())
    if n == 0:
        print ("Case #{}: {}".format(i,  "INSOMNIA"))
    else:
        print ("Case #{}: {}".format(i,  lastNumber(n)))
