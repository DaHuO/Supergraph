f= open("A-large.in", 'r')
output = open("output.txt", 'w')

t = f.readline()
t = int(t)
case = 1

for a0 in xrange(t):
    num = f.readline()
    num = int(num)
    allDigits = False
    digits = {}
    digBase = "0123456789"
    for dig in digBase:
        digits[dig] = 0
    for x in xrange(1,101):
        if allDigits:
            continue
        xN = num * x
        xN = str(xN)
        for digit in xN:
            digits[digit] += 1
        allDigits = True
        for key in digits.keys():
            if digits[key] == 0:
                allDigits = False
    output.write("Case #" + str(case) + ": ")
    if allDigits:
        output.write(xN + '\n')
    else:
        output.write("Insomnia\n")
    case += 1
        
output.close()
f.close()