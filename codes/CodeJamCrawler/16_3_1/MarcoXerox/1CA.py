from string import ascii_uppercase
for t in range(1,int(input())+1):
    n = int(input())
    m = list(zip(map(int,input().split()),ascii_uppercase))
    a = list()
    while True:
        s = sum(x[0] > 0 for x in m)
        m.sort()
        if s == 3:
            if m[-3][0] == m[-2][0] == m[-1][0] == 1:
                m[-1] = (m[-1][0]-1, m[-1][1])
                a.append(m[-1][1])
                continue
        if s >= 2:
            m[-2] = (m[-2][0]-1, m[-2][1])
            m[-1] = (m[-1][0]-1, m[-1][1])
            a.append(m[-2][1] + m[-1][1])
        elif s:
            m[-1] = (m[-1][0]-1,m[-1][1])
            a.append(m[-1][1])
        else:
            break
    print(*(["Case #%d:" % t] + a))
