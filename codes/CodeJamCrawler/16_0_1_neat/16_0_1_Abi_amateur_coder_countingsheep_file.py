def ans(n):
    if n == 0:
        return 'INSOMNIA'
    else:
        # s = ['0','1','2','3','4','5','6','7','8','9']
        t = []
        m = 0
        while len(t) != 10:
            m += n
            s_m = str(m)
            for j in s_m:
                if j not in t:
                    t.append(j)
        return s_m

def main():
    i_filename = 'A-large.in'
    o_filename = 'out.txt'
    h = open(i_filename, 'r')
    g = open(o_filename, 'w')
    l = h.readline()
    t = int(l[:-1])
    for i in range(1, t + 1):
        l = h.readline()
        n = int(l[:-1])
        c = str(i)
        g.write('Case #')
        g.write(str(i))
        g.write(': ')
        g.write(ans(n))
        g.write('\n')
    h.close()
    g.close()

main()
