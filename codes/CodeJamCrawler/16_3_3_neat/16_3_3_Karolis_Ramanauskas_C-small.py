from random import shuffle


def solve(pp):
    J, P, S, K = [int(i) for i in pp.split()]
    print J, P, S, K
    sets = []
    for j in range(J):
        for p in range(P):
            for s in range(S):
                sets.append([j, p, s])
    print len(sets), sets
    best = []
    for i in range(100):
        shuffle(sets)
        used = []
        used01 = {}
        used02 = {}
        used12 = {}
        sc = 0
        for i in range(100):
            # print "step #" + str(i)
            minsc = 999
            mins = ''
            for s in sets:
                k = max(max(used01.values() or [0]), max(used02.values() or [0]), max(used12.values() or [0]))
                sc = 0
                if ''.join([str(s[0]), str(s[1])]) in used01.keys():
                    sc += 1
                    k = max(k, used01[''.join([str(s[0]), str(s[1])])]+1)
                if ''.join([str(s[0]), str(s[2])]) in used02.keys():
                    sc += 1
                    k = max(k, used02[''.join([str(s[0]), str(s[2])])]+1)
                if ''.join([str(s[1]), str(s[2])]) in used12.keys():
                    sc += 1
                    k = max(k, used12[''.join([str(s[1]), str(s[2])])]+1)
                # print "sc=" + str(sc) + " minsc=" + str(minsc) + " s=" + str(s) + " used=" + str(used)
                if sc < minsc and s not in used and k <= K:
                    minsc = sc
                    mins = s
            if mins == '':
                break
            # print minsc, mins
            used.append(mins)
            used01[''.join([str(mins[0]), str(mins[1])])] = used01.get(''.join([str(mins[0]), str(mins[1])]), 0) + 1
            used02[''.join([str(mins[0]), str(mins[2])])] = used02.get(''.join([str(mins[0]), str(mins[2])]), 0) + 1
            used12[''.join([str(mins[1]), str(mins[2])])] = used12.get(''.join([str(mins[1]), str(mins[2])]), 0) + 1
            # print used, used01, used02, used12
        if len(best) < len(used):
            best = used

    return best


def main():
    f_in = open('C-small-attempt3.in', 'r')
    # f_in = open('C-small-test.in', 'r')
    f_out = open('C-small.out', 'w')
    T = int(f_in.readline())
    suma = 0
    for i in range(T):
        p = f_in.readline()
        used = solve(p.strip())
        s = "Case #{}: {}\n".format(i+1, len(used))
        for u in used:
            s += ' '.join([str(uu+1) for uu in u]) + '\n'
        suma += len(used)
        print s
        f_out.write(s)
    print suma
    f_in.close()
    f_out.close()

if __name__ == '__main__':
    main()
