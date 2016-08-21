tests = int(raw_input())
for i in xrange(1, tests+1):
    # main logic
    original_num = int(raw_input())
    num = original_num

    digits = [0,0,0,0,0,0,0,0,0,0]
    multiple = 1

    while(True):
        # Check for INSOMNIA
        if multiple == 2000 or original_num == 0:
            num = -1
            break

        #print multiple
        num = original_num*multiple
        multiple += 1

        for digit in str(num):
            digits[int(digit)] += 1

        #print digits

        finished = True
        for j in range(10):
            if digits[j] == 0:
                finished = False

        if finished == True:
            break

    if num != -1:
        print "Case #{}: {}".format(i, num)
    else:
        print "Case #{}: {}".format(i, "INSOMNIA")
