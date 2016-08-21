def accountForDigit(digitsList, digit):
    if digitsList[digit] == 0:
        digitsList[digit] = 1
    return

def count(N):
    digits = [0,0,0,0,0,0,0,0,0,0]
    nextN = N
    i = 0
    if N == 0 :
        return "INSOMNIA"

    while sum(digits) < 10:
        i = i+1
        nDigits = str(nextN)
        for nDigit in nDigits:

            accountForDigit(digits, int(nDigit))

        nextN = N*(i+1)
    return str(i*N)

def main():
    T = int(raw_input())
    for i in range(1,T+1):
        print "Case #%d: %s" % (i, count(int(raw_input())))

main()
