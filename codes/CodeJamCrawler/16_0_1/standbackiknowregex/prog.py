def lastword(word):
    ret = ''
    for c in word:
        if ret == '':
            ret = c
            continue
        if c < ret[0]:
            ret += c
        else:
            ret = c + ret
    return ret

f = open("A-large.in")

t = int(f.readline())
tcs = [x for x in f.readlines()]

o = open("A-large.out", "w")
for ix, tc in enumerate(tcs):
    res = lastword(tc.strip())
    o.write("Case #{}: {}\n".format(ix+1, res))


