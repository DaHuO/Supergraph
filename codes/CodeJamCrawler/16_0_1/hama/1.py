fin = open("A-large.in", 'r')
fout = open("large.out", 'w')

t = int(fin.readline())

def digit_all(digits):
    for digit in digits:
        if digit == 0:
            return False
    return True

limit = 1000
for i in range(t):
    n = int(fin.readline())
    ans = ""
    if n == 0:
        ans = "Case #%d: INSOMNIA\n" % (i+1)
    else:
        cnt = 0
        digits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for j in range(limit):
            cnt = j+1
            multin = cnt * n
            while multin > 0:
                digits[multin % 10] += 1
                multin = int(multin / 10)
            if digit_all(digits):
                break
        if not(digit_all(digits)):
            ans = "Case #%d: UNREACHABLE\n" % (i+1)
        else:
            ans = "Case #%d: %d\n" % (i+1, cnt*n)
    fout.write(ans)

fin.close()
fout.close()
