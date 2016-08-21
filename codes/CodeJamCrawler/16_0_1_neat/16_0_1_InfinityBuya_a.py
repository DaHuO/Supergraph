ALL_DIGITS = set("1234567890")
t = int(raw_input())
for i in xrange(1, t + 1):
    #n, m = [int(s) for s in raw_input().split(" ")]
    n = int(raw_input())
    if n == 0:
        print "Case #{}: {}".format(i, "INSOMNIA")
        continue

    current_digits = set()
    counter = 1
    while current_digits != ALL_DIGITS and n != 0:
        number = n * counter
        current_digits.update(set(str(number)))
        counter += 1
    
    print "Case #{}: {}".format(i, number)