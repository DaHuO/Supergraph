f = open('ALarge.in','r')
l = f.readlines()
f.close()

for i in range(1,len(l)):
    line = l[i].strip()
    seen = set(list(line))
    line = int(line)
    if line == 0:
        print('Case #{}: INSOMNIA'.format(i))
    else:
        current = line
        while len(seen) < 10:
            current += line
            for c in str(current):
                seen.add(c)
        print('Case #{}: {}'.format(i,current))

