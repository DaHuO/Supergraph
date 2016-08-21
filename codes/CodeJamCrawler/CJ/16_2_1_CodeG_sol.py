#!/usr/bin/python

numbers = ["ERO", "NE", "TO", "THEE", "FOR", "IVE", "SI", "EVEN", "EIHT", "NIN"]
unique_even = ['Z', '-1', 'W', '-1', 'U', '-1', 'X', '-1', 'G', '-1']
unique_odd = ['-1', 'O', '-1', 'R', '-1', 'F', '-1', 'S', '-1', 'E']

t = int(raw_input())

for i in range(t):
    val = raw_input()
    out = []
    for u in range(len(unique_even)):
        if unique_even[u] in val:
            indices = [ii for ii, x in enumerate(val) if x == unique_even[u]]
            val = val.replace(unique_even[u], '+', len(indices))
            for c in numbers[u]:
                val = val.replace(c, '+', len(indices))
            out += ([str(u)] * len(indices))
    for u in range(len(unique_odd)):
        if unique_odd[u] in val:
            indices = [ii for ii, x in enumerate(val) if x == unique_odd[u]]
            val = val.replace(unique_odd[u], '+', len(indices))
            for c in numbers[u]:
                val = val.replace(c, '+', len(indices))
            out += ([str(u)] * len(indices))

    out.sort()

    print "Case #" + str(i + 1) + ":", ''.join(out)
