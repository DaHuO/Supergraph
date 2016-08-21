ncases = int(input())
for i in range(ncases):
    num = int(input())
    digits = [0]*10
    last_mul = 0
    for j in range(1,99999):
        found = False
        num_mul = j*num
        if num_mul == last_mul:
            print "Case #%i: INSOMNIA"%(i+1)
            break
        while num_mul:
            num_mul, rem = divmod(num_mul,10)
            digits[rem] = 1
            if sum(digits) == 10:
                found = j*num
                break
        if found:
            print "Case #%i: %i"%(i+1, found)
            break
