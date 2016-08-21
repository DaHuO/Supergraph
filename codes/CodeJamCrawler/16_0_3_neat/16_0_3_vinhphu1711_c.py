def check(s):
    flag = False
    for b in range(2, 11):
        d = b+1
        if int(s, b) % d != 0:
            flag = True

    return flag

T = int(raw_input())

for t in range(T):
    N, J = [int(i) for i in raw_input().split()]
    
    format_str = '0%db' % (N-3)

    print 'Case #%d:' % (t+1)

    oprd1 = 0b11
    
    i = 0
    num = 0
    while i < J and num < 2 ** (N-3):
        bin_str = '1' + format(num, format_str) + '1'
        oprd2 = int(bin_str, 2)

        if oprd2 > ((2 ** N) - 1) / oprd1:
            break

        s = format(oprd1 * oprd2, 'b')

        if check(s):
            num += 1
            continue
        print s, ' '.join([str(int(format(oprd1, 'b'), b)) for b in range(2, 11)])


        num += 1
        i += 1
    