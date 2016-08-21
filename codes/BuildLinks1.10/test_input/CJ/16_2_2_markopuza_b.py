def find(a, b, pos):
    #print(a + " " + b)
    if not '?' in (a + b):
        return (abs(int(a)-int(b)), a, b)

    if a[pos] != '?' and b[pos] != '?':
        return find(a, b, pos + 1)
    if a[pos] == '?' and b[pos] != '?':
        ps = [find(a[:pos] + d + a[pos+1:], b, pos + 1) for d in map(str,range(10))]
        return sorted(ps)[0]
    if a[pos] != '?' and b[pos] == '?':
        ps = [find(a, b[:pos] + d + b[pos+1:], pos + 1) for d in map(str,range(10))]
        return sorted(ps)[0]
    if a[pos] == '?' and b[pos] == '?':
        ps = [find(a[:pos] + d1 + a[pos+1:], b[:pos] + d2 + b[pos+1:], pos + 1) for d1 in map(str,range(10)) for d2 in map(str, range(10))]
        return sorted(ps)[0]

for t in range(1, int(input())+1):
    c, j = input().split()
    l = len(c)
    res = find(c, j, 0)
    print('Case #' + str(t) + ': ' + res[1] + ' ' + res[2])
