def place (w, l):
    if len(w) == 0 or l > w[0]:
        w.insert(0, l)
        return

    i = 0
    while i < len(w) and l == w[i]:
        i += 1
    if i == len(w) or l > w[i]:
        w.insert(0, l)

    else:
        w.append(l)

input = 'A-large.in'
output = 'out.txt'

with open(input) as f:
    content = f.readlines()
content = [x.strip('\n') for x in content]


with open(output, 'w') as o:
    for i, c in enumerate(content[1:]):
        w = []
        for l in c:
            place(w, l)

        o.write('Case #%s: ' % (i+1))
        o.write(''.join(w))
        o.write('\n')

        print 'Case #%s: ' % (i+1), ''.join(w)
