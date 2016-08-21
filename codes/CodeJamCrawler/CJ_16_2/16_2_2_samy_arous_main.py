def brute_force(sc1, sc2):
    l = len(sc1)
    x1 = sc1.count('?')
    x2 = sc2.count('?')
    sc1 = sc1.replace('?', '%s')
    sc2 = sc2.replace('?', '%s')
    f1 = "%%0%sd" % x1
    f2 = "%%0%sd" % x2
    m  = None
    b1 = None
    b2 = None

    for l1 in range(10**x1):
        s1 = f1 % l1
        if x1:
            s1 = sc1 % tuple(s1)
        else:
            s1 = sc1
        for l2 in range(10**x2):
            s2 = f2 % l2
            if x2:
                s2 = sc2 % tuple(s2)
            else:
                s2 = sc2
            d = abs(int(s1)-int(s2))
            if m is None or d < m:
                m = d
                b1 = s1
                b2 = s2

    return b1, b2



def solve(sc1, sc2):
    b_sc1 = sc1
    b_sc2 = sc2
    # equal ?
    cmp_flag = 0
    l = len(sc1)
    sc1 = list(sc1)
    sc2 = list(sc2)
    for i in range(l):
        if sc1[i] == '?' and sc2[i] == '?': # both are empty
            if cmp_flag == 0:
                sc1[i] = '0'
                sc2[i] = '0'
            elif cmp_flag == 1: # sc2 is bigger, minimze sc2, maximize sc1
                sc1[i] = '9'
                sc2[i] = '0'
            elif cmp_flag == -1: # sc2 is bigger, minimze sc2, maximize sc1
                sc1[i] = '0'
                sc2[i] = '9'
        elif sc1[i] == '?':
            if cmp_flag == 0:
                sc1[i] = sc2[i]
            elif cmp_flag == 1: # sc2 is bigger, maximize sc1
                sc1[i] = '9'
            elif cmp_flag == -1: # sc1 is bigger, minimze sc1
                sc1[i] = '0'
        elif sc2[i] == '?':
            if cmp_flag == 0:
                sc2[i] = sc1[i]
            elif cmp_flag == 1: # sc2 is bigger, minimize sc2
                sc2[i] = '0'
            elif cmp_flag == -1: # sc1 is bigger, maximize sc2
                sc2[i] = '9'
        elif cmp_flag == 0:
            cmp_flag = 1 if int(sc2[i]) > int(sc1[i]) else -1

    r1, r2 = brute_force(b_sc1, b_sc2)
    sc1 = ''.join(sc1)
    sc2 = ''.join(sc2)
    return b_sc1, b_sc2, sc1, sc2, r1, r2, sc1 == r1 and sc2 == r2





def read_input():
    return raw_input().split()

if __name__ == '__main__':
    t = int(raw_input())
    for i in range(t):
        res = map(str, brute_force(*read_input()))
        print "Case #%s: %s" % ( i+1, " ".join(res) )

    # test_cases = [
    #     ('1?', '2?',),
    #     ('?2?', '??3',),
    #     ('?', '?',),
    #     ('?5', '?0',),
    # ]
    # for i, test in enumerate(test_cases):
    #     res = map(str, brute_force(*test))
    #     print "Case #%s: %s" % ( i+1, " ".join(res) )