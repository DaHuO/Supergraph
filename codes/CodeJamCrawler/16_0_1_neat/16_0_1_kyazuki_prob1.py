T = input()
N = []
for i in xrange(T):
    N.append(str(input()))

case_num = 1
for i in N:
    if i == '0':
        print "Case #{}: INSOMNIA".format(case_num)
        case_num += 1
        continue
 
    a = []
    prod_num = 1
    j_list = map(str, xrange(10))
    while len(a) != 10:
        for j in j_list:
            if j not in a:
                if j in str(int(i)*prod_num):
                    a.append(j)
        prod_num += 1

    print "Case #{}: {}".format(case_num, int(i)*(prod_num-1))
    case_num += 1


