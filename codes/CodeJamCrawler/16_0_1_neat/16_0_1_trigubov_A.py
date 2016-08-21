f_in = open('A-large.in.txt')
f_out = open('out.txt', 'w')
t = int(f_in.readline())
ok = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
for j in range(1, t + 1):
    test_case = set()
    n = int(f_in.readline())
    i = 1
    off = True
    while off:
        if n is 0:
            # print "Case #{}: INSOMNIA".format(j)
            f_out.write("Case #{}: INSOMNIA".format(j) + '\n')
            off = False

        current = str(n * i)
        for digit in current:
            test_case.add(digit)

        if test_case == ok:
            print "Case #{}: {}".format(j, current)
            f_out.write("Case #{}: {}".format(j, current) + '\n')
            off = False
        i += 1


