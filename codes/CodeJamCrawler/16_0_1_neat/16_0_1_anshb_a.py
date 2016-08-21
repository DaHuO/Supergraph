def calc_digits(arr):
    s = 0
    m = 1
    for i in arr:
        s += i
        m *= i
    return s, m

def found_digits(arr, digit):
    digit = list(str(digit))
    for i in digit:
        arr[int(i)] += 1

T = int(raw_input())
for t0 in xrange(1, T+1):
    N = int(raw_input())

    if N == 0:
        print "Case #"+str(t0)+":", "INSOMNIA"
        continue

    digits = [0]*10
    SUM, MUL = calc_digits(digits)
    i = 0
    
    while MUL == 0:
        i += 1
        found_digits(digits, N*i)
        SUM, MUL = calc_digits(digits)
    else:
        print "Case #"+str(t0)+":", N*i
# print "Done"