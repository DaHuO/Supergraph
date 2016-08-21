cases = int(raw_input())
for case in range(cases):
    dic = {}
    l = []
    out = []
    size = int(raw_input())
    for i in range(size * 2 -1):
        line_in = raw_input().strip().split(' ')
        l.append(line_in)
    l.sort()
    for r in l:
        for c in r:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1
    for key in dic:
        if dic[key] % 2 == 1:
            out.append(int(key))
    out.sort()
    out = map(str, out)
    line_out = " ".join(out)
    print("Case #" + str(case+1) + ": " + line_out)
