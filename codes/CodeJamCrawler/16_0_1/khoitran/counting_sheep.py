def get_sheep_val(n):
    if n == 0:
        return "INSOMNIA"

    c = [0 for i in range(0, 10)]
    digit_left = 10
    cur = n 
    i = 0
    while digit_left > 0:
        i = i + 1
        num = n * i
        while num > 0:
            m = num % 10
            if c[m] == 0:
                digit_left = digit_left - 1
                c[m] = 1
            num = num / 10
    return i * n
        

if __name__ == "__main__":
    testcases = input()
     
    for caseNr in xrange(1, testcases+1):
        cipher = raw_input()
        print("Case #%i: %s" % (caseNr, get_sheep_val(int(cipher))))

