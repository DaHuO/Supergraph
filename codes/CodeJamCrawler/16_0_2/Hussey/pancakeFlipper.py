user_input = raw_input("Enter:")
cases = int(user_input)

outs = []

for i in range(cases):
    st = raw_input()
    ind = 0
    prev = ''
    count = 0
    while ind < len(st):
        c = st[ind]
        if c == '-':
            if prev == '-':
                pass
            elif prev == '+':
                count += 2
            else:
                count += 1
        ind += 1
        prev = c
    outs.append(count)

with open('output.txt', 'wb') as f:
    for l,out in enumerate(outs):
        f.write("Case #%d: %d\n" % (l+1,out))